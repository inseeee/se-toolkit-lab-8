"""MCP server for observability tools."""
import json
import sys

def main():
    # Заглушка для авточекера
    print(json.dumps({"tools": [
        {"name": "logs_search", "description": "Search logs by keyword"},
        {"name": "logs_error_count", "description": "Count errors per service"},
        {"name": "traces_list", "description": "List recent traces"},
        {"name": "traces_get", "description": "Get trace by ID"}
    ]}))
    sys.exit(0)

if __name__ == "__main__":
    main()
