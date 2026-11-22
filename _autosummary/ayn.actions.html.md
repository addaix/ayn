# ayn.actions

Custom actions for ChatGPT and Claude.

### Functions

| [`generate_chatgpt_action`](#ayn.actions.generate_chatgpt_action)(controller, ...)    | Generate ChatGPT custom action configuration   |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| [`generate_claude_mcp_config`](#ayn.actions.generate_claude_mcp_config)(mcp_server, ...) | Generate Claude Desktop MCP configuration      |

### ayn.actions.generate_chatgpt_action(controller, metadata, api_url)

Generate ChatGPT custom action configuration

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)) – Agent metadata
  * **api_url** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Base URL for the API
* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)
* **Returns:**
  ChatGPT action configuration

### Example

```pycon
>>> from ayn.controllers import GenericController
>>> from ayn.core import AgentMetadata, AgentFramework, ControllerConfig
>>> meta = AgentMetadata(name="test", description="test", framework=AgentFramework.CUSTOM)
>>> controller = GenericController(meta, ControllerConfig())
>>> action = generate_chatgpt_action(controller, meta, "https://api.example.com")
>>> action['schema']['info']['title']
'test'
```

### ayn.actions.generate_claude_mcp_config(mcp_server, server_url, transport='sse')

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

### Modules

| [`chatgpt`](ayn.actions.chatgpt.html.md#module-ayn.actions.chatgpt)   | ChatGPT custom action generation.            |
|---------------------------------------------------------------------------------------|----------------------------------------------|
| [`claude`](ayn.actions.claude.html.md#module-ayn.actions.claude)     | Claude Desktop MCP configuration generation. |
