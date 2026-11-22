# ayn.mcp

Model Context Protocol support.

### Functions

| [`controller_to_mcp_server`](#ayn.mcp.controller_to_mcp_server)(controller, metadata, \*)   | Convert an agent controller to MCP server   |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------|

### Classes

| [`MCPTool`](#ayn.mcp.MCPTool)(name, description, input_schema[, ...])   | MCP tool definition       |
|----------------------------------------------------------------------------------------------------|---------------------------|
| [`MCPResource`](#ayn.mcp.MCPResource)(uri, name[, mimeType, description])   | MCP resource definition   |
| [`MCPPrompt`](#ayn.mcp.MCPPrompt)(name, description[, arguments])         | MCP prompt template       |
| [`MCPServer`](#ayn.mcp.MCPServer)(name[, version, controller])            | MCP Server implementation |

### *class* ayn.mcp.MCPPrompt(name, description, arguments=list())

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP prompt template

### Example

```pycon
>>> prompt = MCPPrompt(
...     name="summarize",
...     description="Summarize text",
...     arguments=[{"name": "text", "description": "Text to summarize", "required": True}]
... )
>>> prompt.name
'summarize'
```

#### to_dict()

Convert to MCP prompt format

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### *class* ayn.mcp.MCPResource(uri, name, mimeType='text/plain', description='')

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP resource definition

### Example

```pycon
>>> resource = MCPResource(
...     uri="file:///data.csv",
...     name="Dataset",
...     mimeType="text/csv"
... )
>>> resource.name
'Dataset'
```

#### to_dict()

Convert to MCP resource format

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### *class* ayn.mcp.MCPServer(name, version='1.0.0', controller=None)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP Server implementation

Exposes agent capabilities via Model Context Protocol.

### Example

```pycon
>>> server = MCPServer(name="test-server")
>>> tool = MCPTool(
...     name="greet",
...     description="Greet user",
...     input_schema={"type": "object", "properties": {}}
... )
>>> server.add_tool(tool)
>>> len(server.tools)
1
```

#### add_prompt(prompt)

Add a prompt to the server

#### add_resource(resource)

Add a resource to the server

#### add_tool(tool)

Add a tool to the server

### Example

```pycon
>>> server = MCPServer("test")
>>> tool = MCPTool("test", "test tool", {})
>>> server.add_tool(tool)
>>> server.tools[0].name
'test'
```

#### handle_call_tool(tool_name, arguments)

Handle tools/call request

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

#### handle_list_prompts()

Handle prompts/list request

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

#### handle_list_resources()

Handle resources/list request

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

#### handle_list_tools()

Handle tools/list request

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

#### to_json_rpc_handler()

Create a JSON-RPC handler for MCP protocol

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)
* **Returns:**
  Handler function that processes JSON-RPC requests

### *class* ayn.mcp.MCPTool(name, description, input_schema, handler=None)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP tool definition

### Example

```pycon
>>> tool = MCPTool(
...     name="search",
...     description="Search for information",
...     input_schema={"type": "object", "properties": {"query": {"type": "string"}}}
... )
>>> tool.name
'search'
```

#### to_dict()

Convert to MCP tool format

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### ayn.mcp.controller_to_mcp_server(controller, metadata, , tools=None, resources=None, prompts=None)

Convert an agent controller to MCP server

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)) – Agent metadata
  * **tools** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MCPTool`](ayn.mcp.models.html.md#ayn.mcp.models.MCPTool)]]) – Optional tools to expose
  * **resources** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MCPResource`](ayn.mcp.models.html.md#ayn.mcp.models.MCPResource)]]) – Optional resources to expose
  * **prompts** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MCPPrompt`](ayn.mcp.models.html.md#ayn.mcp.models.MCPPrompt)]]) – Optional prompts to expose
* **Return type:**
  [`MCPServer`](ayn.mcp.server.html.md#ayn.mcp.server.MCPServer)
* **Returns:**
  MCP server instance

### Example

```pycon
>>> from ayn.controllers import GenericController
>>> from ayn.core import AgentMetadata, AgentFramework, ControllerConfig
>>> meta = AgentMetadata(name="test", description="test", framework=AgentFramework.CUSTOM)
>>> controller = GenericController(meta, ControllerConfig())
>>> server = controller_to_mcp_server(controller, meta)
>>> server.name
'test'
```

### Modules

| [`models`](ayn.mcp.models.html.md#module-ayn.mcp.models)   | MCP data models.           |
|---------------------------------------------------------------------------------|----------------------------|
| [`server`](ayn.mcp.server.html.md#module-ayn.mcp.server)   | MCP server implementation. |
