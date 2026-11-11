:ON ERROR EXIT
USE DatabaseWikiLab;
GO
SET NOCOUNT ON;
SET XACT_ABORT ON;

IF SCHEMA_ID(N'LabPerf') IS NULL
    EXEC(N'CREATE SCHEMA LabPerf AUTHORIZATION dbo;');

IF OBJECT_ID(N'LabPerf.Payment', N'U') IS NULL
BEGIN
    CREATE TABLE LabPerf.Payment
    (
        PaymentId bigint NOT NULL PRIMARY KEY,
        TenantId int NOT NULL,
        AccountId bigint NOT NULL,
        CreatedAt datetime2(0) NOT NULL,
        Amount decimal(19,4) NOT NULL,
        Currency char(3) NOT NULL,
        Payload char(100) NOT NULL
    );

    ;WITH Digits AS
    (
        SELECT n FROM (VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) AS v(n)
    ), Numbers AS
    (
        SELECT 1 + a.n + 10*b.n + 100*c.n + 1000*d.n + 10000*e.n AS n
        FROM Digits AS a CROSS JOIN Digits AS b CROSS JOIN Digits AS c
        CROSS JOIN Digits AS d CROSS JOIN Digits AS e
    )
    INSERT LabPerf.Payment
        (PaymentId, TenantId, AccountId, CreatedAt, Amount, Currency, Payload)
    SELECT n, 1,
           CASE WHEN n % 100 < 80 THEN 1 ELSE 2 + n % 1000 END,
           DATEADD(day, n % 730, CONVERT(datetime2(0), '20250101')),
           CONVERT(decimal(19,4), 1 + n % 10000), 'USD', REPLICATE('x', 100)
    FROM Numbers;
END;

-- Nếu chạy lại, index có thể đã tồn tại: đây không còn là baseline chưa index.
-- Để đo cả hai trạng thái từ đầu, dùng database lab mới theo hướng dẫn.
DECLARE @AccountId bigint = 1;
DECLARE @From datetime2(0) = '20260101', @To datetime2(0) = '20270101';
DECLARE @CountBefore bigint, @CountAfter bigint;
DECLARE @SumBefore decimal(38,4), @SumAfter decimal(38,4);

SET STATISTICS IO ON;
SET STATISTICS TIME ON;

SELECT @CountBefore = COUNT_BIG(*), @SumBefore = SUM(Amount)
FROM LabPerf.Payment
WHERE TenantId = 1 AND AccountId = @AccountId AND YEAR(CreatedAt) = 2026;

IF NOT EXISTS
(
    SELECT 1 FROM sys.indexes
    WHERE object_id = OBJECT_ID(N'LabPerf.Payment')
      AND name = N'IX_LabPerf_AccountTime'
)
    CREATE INDEX IX_LabPerf_AccountTime
    ON LabPerf.Payment (TenantId, AccountId, CreatedAt)
    INCLUDE (Amount, Currency);

SELECT @CountAfter = COUNT_BIG(*), @SumAfter = SUM(Amount)
FROM LabPerf.Payment
WHERE TenantId = 1 AND AccountId = @AccountId
  AND CreatedAt >= @From AND CreatedAt < @To;

SET STATISTICS TIME OFF;
SET STATISTICS IO OFF;

IF @CountBefore <> @CountAfter
   OR COALESCE(@SumBefore, 0) <> COALESCE(@SumAfter, 0)
    THROW 51920, N'Kết quả trước/sau khác nhau.', 1;

SELECT @CountBefore AS RowsBefore, @CountAfter AS RowsAfter,
       @SumBefore AS AmountBefore, @SumAfter AS AmountAfter;

-- Bài tập: đo account nhỏ (ví dụ 82) và account lớn (1), actual plan,
-- warm-cache/cold-cache trên lab riêng; đo chi phí ghi của index.
-- Hai yếu tố đã đổi: predicate và index. Muốn phân tích nguyên nhân,
-- đo ma trận 2x2: có/không index x YEAR/range, không kết luận từ một cặp chạy.
GO
