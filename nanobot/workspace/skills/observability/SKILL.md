# Observability Skills

You have access to observability tools:
- `logs_search` – search logs by keyword and time range
- `logs_error_count` – count errors per service
- `traces_list` – list recent traces for a service
- `traces_get` – fetch a trace by ID

When asked about errors:
1. First check logs for errors
2. If trace_id found, fetch full trace
3. Summarize findings concisely
