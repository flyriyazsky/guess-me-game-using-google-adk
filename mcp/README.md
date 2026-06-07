# MCP Server Setup & Usage Guide

This directory contains the Model Context Protocol (MCP) server implementation with tools for integer operations and long-running tasks.

## Prerequisites

- Python 3.12+
- `uv` package manager (or pip)
- Virtual environment activated

## Setup Instructions

### 1. Install `uv` (if not already installed)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv
```

### 2. Create and Activate Virtual Environment

```bash
cd /Users/riyaz/google-adk

# Create virtual environment (one time)
python3.12 -m venv venv

# Activate virtual environment
# macOS / Linux:
source venv/bin/activate

# Windows PowerShell:
# .\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
cd mcp
pip install -r requirements.txt
# OR
uv pip install -r requirements.txt
```

The `pyproject.toml` includes `mcp[cli]>=1.27.2` as a dependency.

## Running the MCP Server

### Option 1: Development Mode (with hot reload)

```bash
cd /Users/riyaz/google-adk/mcp
mcp dev main.py
```

This watches the file for changes and automatically restarts the server.

### Option 2: Using `uv` directly

```bash
cd /Users/riyaz/google-adk/mcp
uv run --with mcp mcp run main.py
```

### Option 3: Standard Python execution

```bash
cd /Users/riyaz/google-adk/mcp
python main.py
```

## Accessing the MCP Server

Once the server is running (via any of the methods above), it exposes the following tools:

- **add_integer(a, b)** — Adds two integers and returns the sum
- **subtract_integer(a, b)** — Subtracts the second integer from the first
- **divide_integer(a, b)** — Divides two floats and returns the quotient
- **long_running_task(duration)** — Simulates a long-running task by sleeping for the specified duration (in seconds)

## Logging

The MCP server logs all tool invocations to `mcp/mcp.log`.

### Log Configuration

Logs are automatically written to:
```
/Users/riyaz/google-adk/mcp/mcp.log
```

### Log Format

```
2026-06-07 14:55:52,123 - INFO - Adding integers: 5 + 3
2026-06-07 14:55:53,456 - INFO - Subtracting integers: 10 - 4
```

### Viewing Logs

```bash
# Real-time log monitoring
tail -f mcp.log

# View entire log
cat mcp.log

# Clear logs
> mcp.log
```

### Tool Logging Examples

When a tool is called, it automatically logs:

- `add_integer(5, 3)` → Logs: `Adding integers: 5 + 3`
- `subtract_integer(10, 4)` → Logs: `Subtracting integers: 10 - 4`
- `divide_integer(20, 4)` → Logs: `Dividing floats: 20 / 4`
- `long_running_task(10)` → Logs: `Starting long-running task for 10 seconds.` + progress updates

## Troubleshooting

### Server fails to start
- Ensure you're in the `/Users/riyaz/google-adk/mcp` directory
- Verify the virtual environment is activated: `which python` should show the venv path
- Check that MCP is installed: `pip list | grep mcp`

### Logs not appearing
- Call a tool to generate logs (logs only appear when tools are invoked)
- Verify the `mcp.log` file exists: `ls -la mcp.log`
- Check file permissions: `chmod 644 mcp.log`

### Import errors
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
- Verify Python version: `python --version` (should be 3.12+)

## Development

To add new tools, add decorated functions to `main.py`:

```python
@mcp.tool()
def my_tool(param: str) -> str:
    '''
    Tool description for documentation.
    Arguments:
    param (str): Parameter description.
    Returns: str: Return value description.
    '''
    logger.info(f"my_tool called with param={param}")
    return f"Result: {param}"
```

The tool will automatically be exposed by the server.

## References

- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Library](https://github.com/jlouis/fastmcp)
- [uv Package Manager](https://astral.sh/uv/)
