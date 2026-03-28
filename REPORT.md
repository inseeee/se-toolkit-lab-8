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
