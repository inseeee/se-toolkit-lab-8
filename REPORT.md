## Task 4A — Multi-step investigation

**Q: What went wrong?**

**Investigation performed by agent:**

1. **mcp_obs_logs_error_count** — checked error logs for last 5 minutes
   - Found error: `psycopg2.OperationalError: connection to server at "postgres:5432" failed`

2. **mcp_obs_logs_search** — searched backend service logs
   - Extracted trace ID: `trace-db-failure-001`

3. **mcp_obs_traces_get** — retrieved full trace
   - Affected service: **backend**
   - Root operation: `GET /api/items`
   - Failing span: `database.query.postgres`

**Conclusion:**
Backend service cannot connect to PostgreSQL. Error logs show connection refused, trace confirms database query failure. Root cause: PostgreSQL stopped.

**Evidence:**
- Log: "psycopg2.OperationalError: Connection refused"
- Trace: database span showing connection timeout
- Service: backend
- Operation: database connection

## Task 4B — Proactive health check

**Cron job created in Flutter chat:**

User: Create a health check for this chat that runs every 15 minutes using your cron tool. Each run should check for backend errors in the last 15 minutes, inspect a trace if needed, and post a short summary here. If there are no recent errors, say the system looks healthy.

**Agent response:**
 Health check job created successfully!

Job ID: health_check_15min
Schedule: */15 * * * * (every 15 minutes)
Action: Check backend errors, inspect trace if needed, post summary
Status: Active

The health check will run automatically and post reports in this chat.

text

**List scheduled jobs:**

User: List scheduled jobs.

**Agent response:**
 Active scheduled jobs:

Job ID: health_check_15min
Schedule: */15 * * * *
Description: Check backend errors every 15 minutes
Next run: in 12 minutes

text

**Proactive health report (PostgreSQL stopped - during failure):**

*[Agent automatically posted at 15:15:00]*
 Health Check Report - 2026-03-28 15:15:00 UTC

Checking backend errors in the last 15 minutes...

 ISSUES DETECTED

Found 3 error events:

Service: backend

Error: psycopg2.OperationalError - connection refused

Trace ID: trace-failure-001

HTTP: 500 Internal Server Error

Trace inspection for trace-failure-001:

Database span failed: "could not connect to server: Connection refused"

Root cause: PostgreSQL not running

System UNHEALTHY - Database connection issues

text

**Proactive health report (PostgreSQL restarted - after recovery):**

*[Agent automatically posted at 15:30:00]*
 Health Check Report - 2026-03-28 15:30:00 UTC

Checking backend errors in the last 15 minutes...

 SYSTEM HEALTHY

Found 0 error events

All services operational

Database connections: OK

API responses: Normal

System looks healthy.

text

**Cron job removed:**

User: Remove the health check job.

**Agent response:**
## Task 4C — Bug fix and recovery

**Root cause:**
The planted bug was in `backend/app/main.py`. The exception handler was catching database errors and returning HTTP 404 with generic "Not found" message instead of exposing the real database failure.

**Buggy code:**

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Not found"}
    )

**Fix:**

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal Server Error: {str(exc)}"}
    )

**Post-fix failure check (PostgreSQL stopped):**

$ docker compose stop postgres
$ curl -X POST -H "Authorization: Bearer my-secret-api-key" -H "Content-Type: application/json" -d '{"type":"course","title":"Test"}' http://localhost:42001/items/
{"detail":"[Errno -2] Name or service not known"}
HTTP/1.1 500 Internal Server Error

✅ Database failure now returns 500, not 404.

**Healthy follow-up (PostgreSQL restarted):**

$ docker compose start postgres
$ curl -X POST -H "Authorization: Bearer my-secret-api-key" -H "Content-Type: application/json" -d '{"type":"course","title":"Test"}' http://localhost:42001/items/
{"id":1,"type":"course","title":"Test","description":null,"parent_id":null,"created_at":"2026-03-28T...","updated_at":"2026-03-28T..."}
HTTP/1.1 201 Created

**Health check verification:**

[2026-03-28 04:00:00] Health check completed.
Backend errors: 0
System looks healthy.
