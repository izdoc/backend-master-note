:ON ERROR EXIT
-- SQLCMD mode. SQL Server 2022, database lab mới và trống. Chạy một lần.
USE DatabaseWikiLab;
GO
SET NOCOUNT ON;
SET XACT_ABORT ON;

IF SCHEMA_ID(N'LabFinance') IS NOT NULL
    THROW 51000, N'Schema đã tồn tại; hãy dùng database lab mới.', 1;
GO
CREATE SCHEMA LabFinance AUTHORIZATION dbo;
GO
CREATE TABLE LabFinance.Account
(
    TenantId int NOT NULL,
    AccountId bigint NOT NULL,
    Currency char(3) NOT NULL,
    OpeningBalance decimal(19,4) NOT NULL,
    Balance decimal(19,4) NOT NULL,
    Version rowversion NOT NULL,
    CONSTRAINT PK_LabAccount PRIMARY KEY (TenantId, AccountId),
    CONSTRAINT UQ_LabAccount_Currency UNIQUE (TenantId, AccountId, Currency),
    CONSTRAINT CK_LabAccount_Balance CHECK (Balance >= 0),
    CONSTRAINT CK_LabAccount_Opening CHECK (OpeningBalance >= 0)
);

CREATE TABLE LabFinance.Journal
(
    TenantId int NOT NULL,
    JournalId bigint IDENTITY(1,1) NOT NULL,
    Currency char(3) NOT NULL,
    PostedAt datetime2(7) NOT NULL
        CONSTRAINT DF_LabJournal_Time DEFAULT SYSUTCDATETIME(),
    CONSTRAINT PK_LabJournal PRIMARY KEY (TenantId, JournalId),
    CONSTRAINT UQ_LabJournal_Currency UNIQUE (TenantId, JournalId, Currency)
);

CREATE TABLE LabFinance.Entry
(
    TenantId int NOT NULL,
    JournalId bigint NOT NULL,
    LineNo smallint NOT NULL,
    AccountId bigint NOT NULL,
    Currency char(3) NOT NULL,
    SignedAmount decimal(19,4) NOT NULL,
    CONSTRAINT PK_LabEntry PRIMARY KEY (TenantId, JournalId, LineNo),
    CONSTRAINT FK_LabEntry_Journal FOREIGN KEY (TenantId, JournalId, Currency)
        REFERENCES LabFinance.Journal (TenantId, JournalId, Currency),
    CONSTRAINT FK_LabEntry_Account FOREIGN KEY (TenantId, AccountId, Currency)
        REFERENCES LabFinance.Account (TenantId, AccountId, Currency),
    CONSTRAINT CK_LabEntry_Amount CHECK (SignedAmount <> 0)
);

CREATE INDEX IX_LabEntry_Account
ON LabFinance.Entry (TenantId, AccountId, JournalId)
INCLUDE (SignedAmount, Currency);

CREATE TABLE LabFinance.TransferRequest
(
    TenantId int NOT NULL,
    IdempotencyKey varchar(100) COLLATE Latin1_General_100_BIN2 NOT NULL,
    FromAccountId bigint NOT NULL,
    ToAccountId bigint NOT NULL,
    Amount decimal(19,4) NOT NULL,
    Currency char(3) NOT NULL,
    JournalId bigint NOT NULL,
    CONSTRAINT PK_LabRequest PRIMARY KEY (TenantId, IdempotencyKey),
    CONSTRAINT UQ_LabRequest_Journal UNIQUE (TenantId, JournalId),
    CONSTRAINT FK_LabRequest_Journal FOREIGN KEY (TenantId, JournalId, Currency)
        REFERENCES LabFinance.Journal (TenantId, JournalId, Currency),
    CONSTRAINT CK_LabRequest_Amount CHECK (Amount > 0),
    CONSTRAINT CK_LabRequest_Accounts CHECK (FromAccountId <> ToAccountId)
);

INSERT LabFinance.Account
    (TenantId, AccountId, Currency, OpeningBalance, Balance)
VALUES
    (1, 1, 'USD', 1000, 1000),
    (1, 2, 'USD', 1000, 1000),
    (1, 3, 'VND', 1000, 1000),
    (2, 4, 'USD', 1000, 1000),
    (1, 5, 'USD', 100, 100),
    (1, 6, 'USD', 100, 100);
GO
