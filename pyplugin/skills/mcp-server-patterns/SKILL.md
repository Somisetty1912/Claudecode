---
name: mcp-server-patterns
description: Build MCP servers with Python SDK — tools, resources, prompts, Pydantic validation, stdio vs HTTP transports. Use official MCP docs for latest API.

---

# MCP Server Patterns (Python)

The Model Context Protocol (MCP) lets AI assistants call tools, read resources, and use prompts from your server. Use this skill when building or maintaining MCP servers in Python. The SDK API evolves; check the official MCP documentation for current method names and signatures.

## When to Use

Use when: implementing a new MCP server, adding tools or resources, choosing stdio vs HTTP, upgrading the SDK, or debugging MCP registration and transport issues.

## How It Works

### Core concepts

- **Tools**: Actions the model can invoke (e.g. search, run a command). Register with `server.tool()` decorator or method.
- **Resources**: Read-only data the model can fetch (e.g. file contents, API responses). Register with `server.resource()` decorator. Handlers receive `uri` as argument.
- **Prompts**: Reusable, parameterized prompt templates the client can surface (e.g. in Claude Desktop). Register with `server.prompt()` decorator.
- **Transport**: stdio for local clients (e.g. Claude Desktop); HTTP is for remote clients (Cursor, cloud).

The Python SDK uses async/await and decorators. Always verify against the current [MCP docs](https://modelcontextprotocol.io).

### Connecting with stdio

For local clients (Claude Desktop), use stdio transport:

```python
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server

async def main():
    server = Server("my-server")
    async with stdio_server(server) as streams:
        await server.wait_for_shutdown()

if __name__ == "__main__":
    asyncio.run(main())
```

Keep server logic (tools + resources) independent of transport so you can plug in stdio or HTTP in the entrypoint.

### Remote (HTTP)

For Cursor, cloud, or other remote clients, use HTTP transport with async server framework (FastAPI, aiohttp).

## Examples

### Install and server setup

```bash
pip install mcp pydantic
```

```python
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from pydantic import BaseModel, Field

# Create server instance
server = Server("my-server")

class ToolInput(BaseModel):
    query: str = Field(description="Search query")

@server.tool()
async def search(query: str) -> str:
    """Search for information"""
    return f"Results for: {query}"

@server.resource()
async def get_resource(uri: str) -> str:
    """Fetch a resource by URI"""
    return f"Content of {uri}"
```

Register tools and resources using decorators or methods. Use **Pydantic** models for input validation. Define the function signature to match the tool parameters; the framework handles schema generation.

## Best Practices

- **Schema first**: Use Pydantic models for type safety and auto-schema generation; document parameters and return types.
- **Async correctness**: Always use `async def` for handlers; await all async operations. Don't block the event loop.
- **Errors**: Return structured errors via exceptions or error responses the model can interpret; avoid raw stack traces.
- **Idempotency**: Prefer idempotent tools where possible so retries are safe.
- **Rate and cost**: For tools that call external APIs, consider rate limits and cost; document in the tool description.
- **Versioning**: Pin SDK version in requirements.txt or pyproject.toml; check release notes when upgrading.
- **Logging**: Use Python logging module for debugging; include request/response IDs for tracing.

## Official SDKs and Docs

- **Python**: `mcp` package on PyPI. Supports async/await, decorators, and Pydantic validation.
- **JavaScript/TypeScript**: `@modelcontextprotocol/sdk` (npm) for Node.js servers.
- **Go**: Official Go SDK on GitHub (`modelcontextprotocol/go-sdk`).
- **C#**: Official C# SDK for .NET.
- **Official Docs**: [modelcontextprotocol.io](https://modelcontextprotocol.io) for latest API specs and examples.
