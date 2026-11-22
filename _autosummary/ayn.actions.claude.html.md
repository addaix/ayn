# ayn.actions.claude

Claude Desktop MCP configuration generation.

### Functions

| [`generate_claude_mcp_config`](#ayn.actions.claude.generate_claude_mcp_config)(mcp_server, ...)   | Generate Claude Desktop MCP configuration   |
|------------------------------------------------------------------------------------------------|---------------------------------------------|

### ayn.actions.claude.generate_claude_mcp_config(mcp_server, server_url, transport='sse')

Generate Claude Desktop MCP configuration

* **Parameters:**
  * **mcp_server** ([`MCPServer`](ayn.mcp.server.html.md#ayn.mcp.server.MCPServer)) – MCP server instance
  * **server_url** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – URL where MCP server is hosted
  * **transport** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Transport type (sse, stdio)
* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)
* **Returns:**
  Claude Desktop MCP config

### Example

```pycon
>>> from ayn.mcp import MCPServer
>>> server = MCPServer("test")
>>> config = generate_claude_mcp_config(server, "http://localhost:8000")
>>> config['mcpServers']['test']['url']
'http://localhost:8000/sse'
```
