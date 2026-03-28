# Task 4 — Diagnose a Failure and Make the Agent Proactive

## Task 4A — Multi-step investigation

**Q: What went wrong?**
**A:** I investigated the system after PostgreSQL was stopped. Error logs showed connection failures. Trace analysis confirmed that the backend service could not connect to the database. The root cause was that the database service was stopped.

---

## Task 4B — Proactive health check

**Scheduled jobs:**
- `health-check` (every 15 minutes) — created via cron tool

**Proactive health report:**
Health check completed.
Backend errors in last 15 minutes: 0
System looks healthy.

---

## Task 4C — Bug fix and recovery

**Root cause:**
The bug was in the exception handler that returned 404 instead of 500 for database connection failures.

**Fix:**
Changed the exception handler to properly return 500 with error details.

**Post-fix failure check:**
Error: connection to database failed (500 Internal Server Error)

**Healthy follow-up:** 
Health check: OK. No errors in last 15 minutes.
