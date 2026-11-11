:ON ERROR EXIT
USE DatabaseWikiLab;
GO
SET NOCOUNT ON;
SET XACT_ABORT ON;

-- Không bọc file bằng transaction ngoài; procedure tự quản transaction.
DECLARE @First TABLE (JournalId bigint, WasReplay bit);
DECLARE @Replay TABLE (JournalId bigint, WasReplay bit);

INSERT @First
EXEC LabFinance.PostTransfer 1, 1, 2, 25, 'USD', 'smoke-transfer-001';
INSERT @Replay
EXEC LabFinance.PostTransfer 1, 1, 2, 25, 'USD', 'smoke-transfer-001';

IF NOT EXISTS
(
    SELECT 1 FROM @First AS f JOIN @Replay AS r ON r.JournalId = f.JournalId
    WHERE r.WasReplay = 1
)
    THROW 51901, N'Replay không trả cùng journal.', 1;

IF (SELECT COUNT(*) FROM LabFinance.TransferRequest
    WHERE TenantId = 1 AND IdempotencyKey = 'smoke-transfer-001') <> 1
    THROW 51902, N'Request bị thiếu hoặc trùng.', 1;

BEGIN TRY
    EXEC LabFinance.PostTransfer 1, 1, 2, 26, 'USD', 'smoke-transfer-001';
    THROW 51903, N'Không phát hiện payload conflict.', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() <> 51003 THROW;
END CATCH;

BEGIN TRY
    EXEC LabFinance.PostTransfer 1, 1, 2, 999999, 'USD', 'smoke-insufficient';
    THROW 51904, N'Không phát hiện thiếu tiền.', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() <> 51006 THROW;
END CATCH;

BEGIN TRY
    EXEC LabFinance.PostTransfer 1, 1, 3, 10, 'USD', 'smoke-currency';
    THROW 51905, N'Không phát hiện sai currency.', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() <> 51005 THROW;
END CATCH;

BEGIN TRY
    EXEC LabFinance.PostTransfer 1, 1, 4, 10, 'USD', 'smoke-tenant';
    THROW 51906, N'Không phát hiện account khác tenant.', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() <> 51004 THROW;
END CATCH;

IF EXISTS
(
    SELECT 1 FROM LabFinance.TransferRequest
    WHERE TenantId = 1
      AND IdempotencyKey IN ('smoke-insufficient', 'smoke-currency', 'smoke-tenant')
)
    THROW 51907, N'Request thất bại còn record committed.', 1;

-- Không có activity khác trên account 1/2 trong smoke dataset.
IF NOT EXISTS (SELECT 1 FROM LabFinance.Account
               WHERE TenantId = 1 AND AccountId = 1 AND Balance = 975)
   OR NOT EXISTS (SELECT 1 FROM LabFinance.Account
                  WHERE TenantId = 1 AND AccountId = 2 AND Balance = 1025)
    THROW 51908, N'Balance không đúng kết quả smoke.', 1;

-- Bao gồm journal không có entry để phát hiện orphan header.
IF EXISTS
(
    SELECT j.TenantId, j.JournalId
    FROM LabFinance.Journal AS j
    LEFT JOIN LabFinance.Entry AS e
        ON e.TenantId = j.TenantId AND e.JournalId = j.JournalId
    GROUP BY j.TenantId, j.JournalId
    HAVING COUNT(e.LineNo) <> 2 OR COALESCE(SUM(e.SignedAmount), 0) <> 0
)
    THROW 51909, N'Journal không cân bằng/không đủ hai dòng.', 1;

IF EXISTS
(
    SELECT a.TenantId, a.AccountId
    FROM LabFinance.Account AS a
    LEFT JOIN LabFinance.Entry AS e
        ON e.TenantId = a.TenantId AND e.AccountId = a.AccountId
    GROUP BY a.TenantId, a.AccountId, a.OpeningBalance, a.Balance
    HAVING a.Balance <> a.OpeningBalance + COALESCE(SUM(e.SignedAmount), 0)
)
    THROW 51910, N'Balance lệch opening cộng entry.', 1;

IF @@TRANCOUNT <> 0
    THROW 51911, N'Bị rò transaction.', 1;

SELECT N'PASS: replay, conflict, validation và các invariant smoke' AS Result;
GO
