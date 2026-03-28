# Task 4 — Diagnose a Failure and Make the Agent Proactive

## Task 4A — Multi-step investigation

**Q: What went wrong?**
A: After stopping PostgreSQL, the backend returned 500 errors. Logs showed "connection refused" to postgres. The trace confirmed the failure occurred in the database connection pool.

## Task 4B — Proactive health check

**Scheduled jobs:**
- health-check (every 2 minutes) — created via cron tool

**Proactive health report:**
[2026-03-28] Health check completed.

Backend errors in last 2 minutes: 0

System looks healthy.

## Task 4C — Bug fix and recovery

**Root cause:**
The planted bug was in `backend/app/main.py` — a broad exception handler was catching database errors and returning 404 instead of 500.

**Fix:**
Modified the exception handler to properly return 500 for database connection errors.

**Post-fix failure check:**
After redeploy and stopping PostgreSQL, request returns 500 Internal Server Error.

**Healthy follow-up:**
After restarting PostgreSQL, health check reports "System looks healthy".
