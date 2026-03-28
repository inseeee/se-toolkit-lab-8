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

**Root cause:** The planted bug was in `backend/app/main.py` exception handler. A broad `except Exception` block caught database connection errors and returned a misleading 404 response instead of propagating the actual error.

**Fix:** Modified `backend/app/main.py` to properly handle database connection errors and return HTTP 500 with error details.

**Post-fix failure check:**
$ curl -H "Authorization: Bearer my-secret-api-key" http://localhost:42002/items/
{"detail":"Internal Server Error: connection to database failed"}
HTTP/1.1 500 Internal Server Error

After the fix, the database failure correctly returns 500, not 404.

**Healthy follow-up:**
After restarting PostgreSQL:
$ curl -H "Authorization: Bearer my-secret-api-key" http://localhost:42002/items/
[{"id":1,"title":"Test Lab 01"}]
HTTP/1.1 200 OK

Health check confirms system is healthy.

---
