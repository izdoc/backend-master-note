:ON ERROR EXIT
USE DatabaseWikiLab;
GO
-- Read-only. Quyền DMV phụ thuộc engine/version; SQL Server 2022 có các DMV
-- yêu cầu VIEW SERVER PERFORMANCE STATE. Không cấp server-wide quyền cho app.
SET NOCOUNT ON;

SELECT name, state_desc, recovery_model_desc, log_reuse_wait_desc,
       is_read_committed_snapshot_on, snapshot_isolation_state_desc
FROM sys.databases
WHERE database_id = DB_ID();

SELECT name, type_desc, size * 8.0 / 1024 AS SizeMB,
       growth, is_percent_growth, physical_name
FROM sys.database_files;

SELECT r.session_id, r.status, r.command, r.blocking_session_id,
       r.wait_type, r.wait_time, r.wait_resource,
       r.cpu_time, r.total_elapsed_time, r.logical_reads,
       r.reads, r.writes, t.text AS BatchText
FROM sys.dm_exec_requests AS r
OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) AS t
WHERE r.database_id = DB_ID() AND r.session_id <> @@SPID;

-- Bao gồm sleeping session có transaction, không chỉ active requests.
-- Transaction có thể chạm nhiều database, vì vậy join theo database transaction.
SELECT s.session_id, s.login_name, s.host_name, s.program_name, s.status,
       a.transaction_id, a.transaction_begin_time,
       DATEDIFF(second, a.transaction_begin_time, SYSDATETIME()) AS AgeSecondsApprox
FROM sys.dm_tran_session_transactions AS st
JOIN sys.dm_tran_active_transactions AS a ON a.transaction_id = st.transaction_id
JOIN sys.dm_tran_database_transactions AS dt ON dt.transaction_id = a.transaction_id
JOIN sys.dm_exec_sessions AS s ON s.session_id = st.session_id
WHERE dt.database_id = DB_ID();

-- Query Store state: không tự bật/tắt cấu hình.
SELECT actual_state_desc, desired_state_desc, readonly_reason,
       current_storage_size_mb, max_storage_size_mb
FROM sys.database_query_store_options;

-- Lưu output ở nơi có quyền phù hợp; BatchText có thể chứa dữ liệu nhạy cảm.
-- transaction_begin_time và SYSDATETIME dùng giờ server; đồng bộ clock khi đối chiếu log.
GO
