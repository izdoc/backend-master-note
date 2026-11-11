:ON ERROR EXIT
USE DatabaseWikiLab;
GO
CREATE OR ALTER PROCEDURE LabFinance.PostTransfer
    @TenantId int,
    @FromAccountId bigint,
    @ToAccountId bigint,
    @Amount decimal(19,4),
    @Currency char(3),
    @IdempotencyKey varchar(100)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    -- Procedure sở hữu transaction; caller không bọc transaction ngoài.
    IF @@TRANCOUNT <> 0
        THROW 51001, N'Không hỗ trợ ambient transaction trong lab.', 1;

    IF @TenantId IS NULL OR @FromAccountId IS NULL OR @ToAccountId IS NULL
       OR @Amount IS NULL OR @Amount <= 0 OR @Currency IS NULL
       OR LEN(@Currency) <> 3 OR @FromAccountId = @ToAccountId
       OR @IdempotencyKey IS NULL OR LEN(@IdempotencyKey) = 0
       OR DATALENGTH(@IdempotencyKey) <> DATALENGTH(LTRIM(RTRIM(@IdempotencyKey)))
        THROW 51002, N'Tham số không hợp lệ.', 1;

    DECLARE @JournalId bigint;
    DECLARE @OldFrom bigint, @OldTo bigint, @OldAmount decimal(19,4), @OldCurrency char(3);
    DECLARE @Low bigint = CASE WHEN @FromAccountId < @ToAccountId
                              THEN @FromAccountId ELSE @ToAccountId END;
    DECLARE @High bigint = CASE WHEN @FromAccountId < @ToAccountId
                               THEN @ToAccountId ELSE @FromAccountId END;
    DECLARE @LowCurrency char(3), @HighCurrency char(3);

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Unique clustered key hỗ trợ lock cả missing-key range.
        -- Mọi caller dùng cùng protocol; hai request cùng key được serialize.
        SELECT @JournalId = JournalId,
               @OldFrom = FromAccountId, @OldTo = ToAccountId,
               @OldAmount = Amount, @OldCurrency = Currency
        FROM LabFinance.TransferRequest WITH (UPDLOCK, HOLDLOCK)
        WHERE TenantId = @TenantId AND IdempotencyKey = @IdempotencyKey;

        IF @JournalId IS NOT NULL
        BEGIN
            IF @OldFrom <> @FromAccountId OR @OldTo <> @ToAccountId
               OR @OldAmount <> @Amount
               OR @OldCurrency COLLATE Latin1_General_100_BIN2
                   <> @Currency COLLATE Latin1_General_100_BIN2
                THROW 51003, N'Key đã được dùng với payload khác.', 1;

            COMMIT TRANSACTION;
            SELECT @JournalId AS JournalId, CAST(1 AS bit) AS WasReplay;
            RETURN;
        END;

        -- Khóa account theo ID tăng dần, cùng thứ tự cho transfer ngược chiều.
        SELECT @LowCurrency = Currency
        FROM LabFinance.Account WITH (UPDLOCK, HOLDLOCK)
        WHERE TenantId = @TenantId AND AccountId = @Low;

        SELECT @HighCurrency = Currency
        FROM LabFinance.Account WITH (UPDLOCK, HOLDLOCK)
        WHERE TenantId = @TenantId AND AccountId = @High;

        IF @LowCurrency IS NULL OR @HighCurrency IS NULL
            THROW 51004, N'Account không tồn tại trong tenant.', 1;

        IF @LowCurrency COLLATE Latin1_General_100_BIN2
               <> @Currency COLLATE Latin1_General_100_BIN2
           OR @HighCurrency COLLATE Latin1_General_100_BIN2
               <> @Currency COLLATE Latin1_General_100_BIN2
            THROW 51005, N'Currency không khớp.', 1;

        UPDATE LabFinance.Account
        SET Balance = Balance - @Amount
        WHERE TenantId = @TenantId AND AccountId = @FromAccountId
          AND Balance >= @Amount;
        IF @@ROWCOUNT <> 1
            THROW 51006, N'Không đủ số dư.', 1;

        UPDATE LabFinance.Account
        SET Balance = Balance + @Amount
        WHERE TenantId = @TenantId AND AccountId = @ToAccountId;
        IF @@ROWCOUNT <> 1
            THROW 51007, N'Không cập nhật được bên nhận.', 1;

        INSERT LabFinance.Journal (TenantId, Currency)
        VALUES (@TenantId, @Currency);
        SET @JournalId = CONVERT(bigint, SCOPE_IDENTITY());

        INSERT LabFinance.Entry
            (TenantId, JournalId, LineNo, AccountId, Currency, SignedAmount)
        VALUES
            (@TenantId, @JournalId, 1, @FromAccountId, @Currency, -@Amount),
            (@TenantId, @JournalId, 2, @ToAccountId, @Currency, @Amount);

        INSERT LabFinance.TransferRequest
            (TenantId, IdempotencyKey, FromAccountId, ToAccountId, Amount, Currency, JournalId)
        VALUES
            (@TenantId, @IdempotencyKey, @FromAccountId, @ToAccountId,
             @Amount, @Currency, @JournalId);

        COMMIT TRANSACTION;
        SELECT @JournalId AS JournalId, CAST(0 AS bit) AS WasReplay;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0 ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO
IF DATABASE_PRINCIPAL_ID(N'LabPoster') IS NULL
    CREATE ROLE LabPoster AUTHORIZATION dbo;
GO
GRANT EXECUTE ON OBJECT::LabFinance.PostTransfer TO LabPoster;
GRANT SELECT ON SCHEMA::LabFinance TO LabPoster;
DENY INSERT, UPDATE, DELETE ON SCHEMA::LabFinance TO LabPoster;
-- Ownership chaining cho phép procedure dbo-owned ghi bảng cùng owner.
-- Không cấp ALTER/CONTROL/DDL cho role này. Dbo/sysadmin bypass quyền runtime.
GO
