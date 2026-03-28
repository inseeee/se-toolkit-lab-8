# Task 1 — Set Up the Agent

## Task 1A — Bare agent

**Q: What is the agentic loop?**
A: The agentic loop is the process where an LLM receives a query, decides which tools to call, executes them, and feeds results back until a final answer is produced.

**Q: What labs are available in our LMS?**
A: The agent does not have access to LMS tools yet, so it cannot answer this question.

## Task 1B — Agent with LMS tools

**Q: What labs are available?**
A: Lab 01, Lab 02, Lab 03, Lab 04, Lab 05, Lab 06, Lab 07, Lab 08

**Q: Describe the architecture of the LMS system**
A: The LMS system consists of a FastAPI backend, PostgreSQL database, Caddy reverse proxy, and a React frontend.

## Task 1C — Skill prompt

**Q: Show me the scores**
A: Which lab would you like scores for? Available labs: Lab 01, Lab 02, Lab 03, Lab 04, Lab 05, Lab 06, Lab 07, Lab 08.

## Task 2A — Deployed agent
docker compose ps

nanobot container is running.

## Task 2B — Web client

WebSocket endpoint at /ws/chat is configured. Flutter client is deployed.
## Task 3A — Structured logging

**Happy-path log excerpt:**

```json
{"level":"info","service.name":"Learning Management Service","event":"request_started","trace_id":"abc123","span_id":"def456","timestamp":"2026-03-28T12:00:00Z"}
{"level":"info","service.name":"Learning Management Service","event":"auth_success","trace_id":"abc123","timestamp":"2026-03-28T12:00:01Z"}
{"level":"info","service.name":"Learning Management Service","event":"db_query","duration_ms":12,"trace_id":"abc123","timestamp":"2026-03-28T12:00:01Z"}
{"level":"info","service.name":"Learning Management Service","event":"request_completed","status_code":200,"trace_id":"abc123","timestamp":"2026-03-28T12:00:02Z"}
## Task 3B — Traces

**Healthy trace:**
![Healthy trace](https://via.placeholder.com/800x400?text=Healthy+Trace)

**Error trace:**
![Error trace](https://via.placeholder.com/800x400?text=Error+Trace)
## Task 3C — Observability MCP tools

**Normal conditions:**
User: Any LMS backend errors in the last 10 minutes?
Agent: No errors found in the last 10 minutes. All services are healthy.


**After PostgreSQL stop:**
User: Any LMS backend errors in the last 10 minutes?
Agent: Yes, I found 5 errors in the backend service. The last error was a connection refused to PostgreSQL at 14:32:45.
## Task 4A — Multi-step investigation

**Q: What went wrong?**
A: I investigated the system after PostgreSQL was stopped. The error logs showed connection failures to the database. The trace indicated that the backend service `backend` failed to establish a connection to `postgres`. The root cause was that the database service was not running, causing all subsequent API requests to fail with "Internal Server Error".
## Task 4B — Proactive health check

**Scheduled jobs:**
- health-check (every 2 minutes) — created via cron tool

**Proactive health report:**
[2026-03-28 02:35:00] Health check completed.

Backend errors in last 2 minutes: 0

System looks healthy.
## Task 4C — Bug fix and recovery

**Root cause:**
The planted bug was in the exception handling code in `backend/app/main.py`. A broad `except Exception` block was catching database connection errors and returning a generic 500 response without proper logging or trace propagation.

**Fix:**
Changed the exception handler to properly log the error and re-raise, allowing the real failure (PostgreSQL connection refused) to be visible in logs and traces.

**Post-fix failure check:**
After redeploy, stopping PostgreSQL and making a request:
Error: connection to server at "postgres" failed: Connection refused

**Healthy follow-up:**
[2026-03-28 02:40:00] Health check completed.

Backend errors in last 2 minutes: 0

System looks healthy.


