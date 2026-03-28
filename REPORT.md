## Task 4A — Multi-step investigation
**Q: What went wrong?**
A: I investigated the system after PostgreSQL was stopped. The error logs showed connection failures to the database. The trace indicated that the backend service `backend` failed to establish a connection to `postgres`. The root cause was that the database service was not running, causing all subsequent API requests to fail with "Internal Server Error".
A: After stopping PostgreSQL, the backend returned 500 errors. Logs showed "connection refused" to postgres. The trace confirmed the failure occurred in the database connection pool.
## Task 4B — Proactive health check
**Cron job created:** health_check_15min
**List scheduled jobs:** health_check_15min - */15 * * * * - Active
**Proactive health report:** System looks healthy

## Task 4C — Bug fix and recovery
**Root cause:** Exception handler fixed
**Fix:** Changed 404 to 500
**Verification:** 
$ curl http://localhost:42002/items/
{"detail":"Database error"}
HTTP/1.1 500 Internal Server Error
