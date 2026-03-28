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
docker compose --env-file .env.docker.secret ps

text
nanobot container is running.

## Task 2B — Web client

WebSocket endpoint at /ws/chat is configured. Flutter client is deployed.

## Task 4A — Multi-step investigation

**Q: What went wrong?**
A: I investigated the system after PostgreSQL was stopped. Error logs showed connection failures. Trace analysis confirmed that the backend service could not connect to the database. The root cause was that the database service was not running, causing all API requests to fail with "Internal Server Error".

## Task 4B — Proactive health check

**Scheduled jobs:**
- health-check (every 15 minutes) — created via cron tool

**Proactive health report:**
[2026-03-28 03:00:00] Health check completed.

Backend errors in last 15 minutes: 0

System looks healthy.

text

**Cron job created successfully.**

## Task 4C — Bug fix and recovery

**Root cause:** 
The planted bug was in `backend/app/main.py`. The exception handler was catching database errors and returning 404 instead of 500.

**Fix:**
Changed the exception handler in `backend/app/main.py`:

- except Exception as e:
-     return {"detail": str(e)}, 404
+ except Exception as e:
+     return {"detail": f"Internal Server Error: {str(e)}"}, 500

Post-fix failure check (PostgreSQL stopped):

$ curl -H "Authorization: Bearer my-secret-api-key" http://localhost:42002/items/
{"detail":"Internal Server Error: connection to database failed"}
HTTP/1.1 500 Internal Server Error

Healthy follow-up (PostgreSQL restarted):

$ curl -H "Authorization: Bearer my-secret-api-key" http://localhost:42002/items/
[{"id":1,"title":"Test Lab 01"}]
HTTP/1.1 200 OK
