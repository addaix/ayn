# ayn

ayn - Agents You Need

A meta-framework for discovering, installing, and integrating reusable AI agents.
Acts as the ‘pip + Docker Hub + Postman’ for AI agents.

Core Features:

1. Search & Discovery: Find agents across GitHub, HuggingFace, awesome lists
2. Standard Controller Interface: Parametrizable agent controllers with action methods
3. HTTP/REST Export: FastAPI and LangServe wrappers
4. MCP Support: Model Context Protocol server integration
5. Custom Actions: ChatGPT and Claude action generation

Architecture:

- Search layer: Unified registry across multiple sources
- Controller protocol: Standard interface for invoking agents
- Export layer: HTTP/REST service generation
- MCP layer: Tools, resources, and prompts
- Actions: OpenAPI specs for ChatGPT/Claude

### Example

```pycon
>>> from ayn import AgentRegistry, BaseAgentController
>>> registry = AgentRegistry()
>>> results = registry.search('data preparation agents')
>>> agent = BaseAgentController.from_metadata(results[0])
>>> result = agent.invoke(input_data)
```

### Functions

| [`export_as_fastapi`](#ayn.export_as_fastapi)(controller[, metadata, ...])     | Export agent controller as FastAPI service   |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------|
| [`export_as_langserve`](#ayn.export_as_langserve)(controller[, metadata])        | Export agent as LangServe compatible service |
| [`controller_to_mcp_server`](#ayn.controller_to_mcp_server)(controller, metadata, \*) | Convert an agent controller to MCP server    |
| [`generate_chatgpt_action`](#ayn.generate_chatgpt_action)(controller, ...)           | Generate ChatGPT custom action configuration |
| [`generate_claude_mcp_config`](#ayn.generate_claude_mcp_config)(mcp_server, ...)        | Generate Claude Desktop MCP configuration    |
| [`create_agent_from_registry`](#ayn.create_agent_from_registry)(registry, query)        | Search registry and create agent controller  |
| [`export_agent_full_stack`](#ayn.export_agent_full_stack)(controller, metadata, \*)  | Export agent with all integrations           |

### Classes

| [`AgentFramework`](#ayn.AgentFramework)(\*values)                        | Supported agent frameworks                         |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [`AgentModality`](#ayn.AgentModality)(\*values)                         | Agent modalities                                   |
| [`AgentMetadata`](#ayn.AgentMetadata)(name, description, framework)     | Metadata for an agent                              |
| [`ControllerConfig`](#ayn.ControllerConfig)([model, temperature, ...])     | Configuration for agent controllers                |
| [`AgentSearcher`](#ayn.AgentSearcher)(\*args, \*\*kwargs)               | Protocol for agent search implementations          |
| [`GitHubAgentSearcher`](#ayn.GitHubAgentSearcher)([github_token])             | Search for agents in GitHub repositories           |
| [`HuggingFaceAgentSearcher`](#ayn.HuggingFaceAgentSearcher)([hf_token])            | Search for agents on Hugging Face                  |
| [`AwesomeListSearcher`](#ayn.AwesomeListSearcher)()                           | Parse and search awesome lists for agents          |
| [`AgentRegistry`](#ayn.AgentRegistry)([searchers, cache_dir])           | Unified registry for searching and managing agents |
| [`AgentController`](#ayn.AgentController)(\*args, \*\*kwargs)             | Standard protocol for agent controllers            |
| [`BaseAgentController`](#ayn.BaseAgentController)(config)                     | Base class for agent controllers                   |
| [`GenericController`](#ayn.GenericController)(metadata, config)             | Generic controller for custom agents               |
| [`CrewAIController`](#ayn.CrewAIController)(metadata, config)              | Controller for CrewAI agents                       |
| [`LangChainController`](#ayn.LangChainController)(metadata, config)           | Controller for LangChain agents                    |
| [`AutoGenController`](#ayn.AutoGenController)(metadata, config)             | Controller for AutoGen agents                      |
| [`MCPTool`](#ayn.MCPTool)(name, description, input_schema[, ...]) | MCP tool definition                                |
| [`MCPResource`](#ayn.MCPResource)(uri, name[, mimeType, description]) | MCP resource definition                            |
| [`MCPPrompt`](#ayn.MCPPrompt)(name, description[, arguments])       | MCP prompt template                                |
| [`MCPServer`](#ayn.MCPServer)(name[, version, controller])          | MCP Server implementation                          |

### *class* ayn.AgentController(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Standard protocol for agent controllers

Controllers provide a uniform interface for invoking agents regardless
of their underlying framework.

### Example

```pycon
>>> class MyController:
...     def __init__(self, config):
...         self.config = config
...     def invoke(self, input_data, **kwargs):
...         return f"Processed: {input_data}"
>>> controller = MyController({'model': 'gpt-4'})
>>> controller.invoke('test')
'Processed: test'
```

#### *async* ainvoke(input_data, \*\*kwargs)

Invoke the agent asynchronously

* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

#### invoke(input_data, \*\*kwargs)

Invoke the agent synchronously

* **Parameters:**
  * **input_data** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any)) – Input data for the agent
  * **\*\*kwargs** – Additional parameters
* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)
* **Returns:**
  Agent output

#### stream(input_data, \*\*kwargs)

Stream agent outputs

* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

### *class* ayn.AgentFramework(\*values)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Supported agent frameworks

### *class* ayn.AgentMetadata(name, description, framework, source='', tags=list(), modality=AgentModality.TEXT, version='0.1.0', author='', license='', dependencies=list(), capabilities=list())

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Metadata for an agent

### Example

```pycon
>>> meta = AgentMetadata(
...     name="data-prep-agent",
...     description="Prepares data for visualization",
...     framework=AgentFramework.CREWAI
... )
>>> meta.name
'data-prep-agent'
```

#### *classmethod* from_dict(data)

Create from dictionary

* **Return type:**
  [`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)

#### to_dict()

Convert to dictionary

### Example

```pycon
>>> meta = AgentMetadata(name="test", description="test agent", framework=AgentFramework.CREWAI)
>>> d = meta.to_dict()
>>> d['name']
'test'
```

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### *class* ayn.AgentModality(\*values)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Agent modalities

### *class* ayn.AgentRegistry(searchers=None, cache_dir=None)

Bases: [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]

Unified registry for searching and managing agents

Aggregates results from multiple sources and provides a dict-like interface.

### Example

```pycon
>>> registry = AgentRegistry()
>>> # Add a local agent
>>> from ayn.core import AgentMetadata, AgentFramework
>>> meta = AgentMetadata(name="test", description="test", framework=AgentFramework.CUSTOM)
>>> registry['test'] = meta
>>> registry['test'].name
'test'
>>> 'test' in registry
True
```

#### search(query, , limit=20, source=None, \*\*filters)

Search across all sources

* **Parameters:**
  * **query** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Search query
  * **limit** ([`int`](https://docs.python.org/3/builtins/functions.html#int)) – Max results
  * **source** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str)]) – Specific source to search (github, huggingface, awesome)
  * **\*\*filters** – Additional filters
* **Return type:**
  [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]
* **Returns:**
  List of agent metadata

### Example

```pycon
>>> registry = AgentRegistry(searchers=[])
>>> # Add some test data
>>> from ayn.core import AgentMetadata, AgentFramework
>>> registry['agent1'] = AgentMetadata(
...     name="agent1", description="test agent",
...     framework=AgentFramework.CREWAI, tags=['data']
... )
>>> results = registry.search('agent')
>>> len(results) >= 1
True
```

### *class* ayn.AgentSearcher(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Protocol for agent search implementations

#### search(query, , limit=20, \*\*filters)

Search for agents

* **Parameters:**
  * **query** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Search query string
  * **limit** ([`int`](https://docs.python.org/3/builtins/functions.html#int)) – Maximum results to return
  * **\*\*filters** – Additional filters (framework, tags, etc.)
* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]
* **Returns:**
  Iterable of agent metadata

### *class* ayn.AutoGenController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for AutoGen agents

Not implemented yet: today this behaves exactly like [`GenericController`](#ayn.GenericController)
(it echoes its input) and does not run an AutoGen agent.
See AYN_IMPLEMENTATION_ROADMAP.md for details

### *class* ayn.AwesomeListSearcher

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Parse and search awesome lists for agents

### Example

```pycon
>>> searcher = AwesomeListSearcher()
>>> results = searcher.search('autogen')
```

#### search(query, , limit=20, \*\*filters)

Search awesome lists

* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]

### *class* ayn.BaseAgentController(config)

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for agent controllers

Provides common functionality and enforces the controller protocol.

### Example

```pycon
>>> class SimpleController(BaseAgentController):
...     def invoke(self, input_data, **kwargs):
...         return f"Result: {input_data}"
>>> controller = SimpleController(ControllerConfig())
>>> controller.invoke('test')
'Result: test'
```

#### *async* ainvoke(input_data, \*\*kwargs)

Default async implementation wraps synchronous invoke

* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

#### *classmethod* from_metadata(metadata, config=None)

Factory method to create controller from metadata

* **Return type:**
  [`BaseAgentController`](ayn.controllers.base.html.md#ayn.controllers.base.BaseAgentController)

#### *abstractmethod* invoke(input_data, \*\*kwargs)

Invoke the agent - must be implemented by subclasses

* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

#### stream(input_data, \*\*kwargs)

Default streaming yields single result

* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

### *class* ayn.ControllerConfig(model='gpt-4', temperature=0.7, max_tokens=1000, timeout=60, retry_count=3, api_key=None, additional_params=dict())

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Configuration for agent controllers

### Example

```pycon
>>> config = ControllerConfig(
...     model="gpt-4",
...     temperature=0.7,
...     max_tokens=1000
... )
>>> config.model
'gpt-4'
```

#### to_dict()

Convert to dictionary

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### *class* ayn.CrewAIController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for CrewAI agents

Not implemented yet: today this behaves exactly like [`GenericController`](#ayn.GenericController)
(it echoes its input) and does not run a CrewAI agent.
See AYN_IMPLEMENTATION_ROADMAP.md for details

### *class* ayn.GenericController(metadata, config)

Bases: [`BaseAgentController`](ayn.controllers.base.html.md#ayn.controllers.base.BaseAgentController)

Generic controller for custom agents

### Example

```pycon
>>> from ayn.core import AgentMetadata, AgentFramework, ControllerConfig
>>> meta = AgentMetadata(name="test", description="test", framework=AgentFramework.CUSTOM)
>>> controller = GenericController(meta, ControllerConfig())
>>> result = controller.invoke({'input': 'test'})
```

#### invoke(input_data, \*\*kwargs)

Generic invoke - subclasses override for specific behavior

* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

### *class* ayn.GitHubAgentSearcher(github_token=None)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Search for agents in GitHub repositories

### Example

```pycon
>>> searcher = GitHubAgentSearcher()
>>> results = searcher.search('crewai agent')
```

#### search(query, , limit=20, \*\*filters)

Search GitHub for agent repos (not implemented: raises `NotImplementedError`)

* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]

### *class* ayn.HuggingFaceAgentSearcher(hf_token=None)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Search for agents on Hugging Face

Uses the Hugging Face MCP tool if available.

### Example

```pycon
>>> searcher = HuggingFaceAgentSearcher()
>>> results = searcher.search('code generation')
```

#### search(query, , limit=20, \*\*filters)

Search Hugging Face for agents

* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]

### *class* ayn.LangChainController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for LangChain agents

Not implemented yet: today this behaves exactly like [`GenericController`](#ayn.GenericController)
(it echoes its input) and does not run a LangChain agent.
See AYN_IMPLEMENTATION_ROADMAP.md for details

### *class* ayn.MCPPrompt(name, description, arguments=list())

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

### *class* ayn.MCPResource(uri, name, mimeType='text/plain', description='')

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

### *class* ayn.MCPServer(name, version='1.0.0', controller=None)

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

### *class* ayn.MCPTool(name, description, input_schema, handler=None)

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

### ayn.controller_to_mcp_server(controller, metadata, , tools=None, resources=None, prompts=None)

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

### ayn.create_agent_from_registry(registry, query, config=None)

Search registry and create agent controller

* **Parameters:**
  * **registry** ([`AgentRegistry`](ayn.registry.base.html.md#ayn.registry.base.AgentRegistry)) – Agent registry
  * **query** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Search query
  * **config** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ControllerConfig`](ayn.core.config.html.md#ayn.core.config.ControllerConfig)]) – Optional controller config
* **Return type:**
  [`BaseAgentController`](ayn.controllers.base.html.md#ayn.controllers.base.BaseAgentController)
* **Returns:**
  Agent controller

### Example

```pycon
>>> from ayn import AgentRegistry
>>> from ayn.core import AgentMetadata, AgentFramework
>>> registry = AgentRegistry(searchers=[])
>>> meta = AgentMetadata(name="test-agent", description="test", framework=AgentFramework.CUSTOM)
>>> registry['test-agent'] = meta
>>> controller = create_agent_from_registry(registry, 'test')
>>> isinstance(controller, BaseAgentController)
True
```

### ayn.export_agent_full_stack(controller, metadata, , api_host='0.0.0.0', api_port=8000, export_fastapi=True, export_mcp=True, export_chatgpt=True, mcp_tools=None)

Export agent with all integrations

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)) – Agent metadata
  * **api_host** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – API host
  * **api_port** ([`int`](https://docs.python.org/3/builtins/functions.html#int)) – API port
  * **export_fastapi** ([`bool`](https://docs.python.org/3/builtins/functions.html#bool)) – Whether to export as FastAPI
  * **export_mcp** ([`bool`](https://docs.python.org/3/builtins/functions.html#bool)) – Whether to export as MCP server
  * **export_chatgpt** ([`bool`](https://docs.python.org/3/builtins/functions.html#bool)) – Whether to generate ChatGPT action
  * **mcp_tools** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`MCPTool`](ayn.mcp.models.html.md#ayn.mcp.models.MCPTool)]]) – Optional MCP tools
* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)
* **Returns:**
  Dict with export artifacts

### Example

```pycon
>>> from ayn.controllers import GenericController
>>> from ayn.core import AgentMetadata, AgentFramework, ControllerConfig
>>> meta = AgentMetadata(name="test", description="test", framework=AgentFramework.CUSTOM)
>>> controller = GenericController(meta, ControllerConfig())
>>> artifacts = export_agent_full_stack(
...     controller, meta,
...     export_fastapi=False, export_mcp=False, export_chatgpt=True
... )
>>> 'chatgpt_action' in artifacts
True
```

### ayn.export_as_fastapi(controller, metadata=None, host='0.0.0.0', port=8000)

Export agent controller as FastAPI service

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]) – Optional agent metadata
  * **host** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Host to bind to
  * **port** ([`int`](https://docs.python.org/3/builtins/functions.html#int)) – Port to bind to

### Example

```pycon
>>> # This would start a server - doctest: +SKIP
>>> controller = GenericController(...)
>>> export_as_fastapi(controller, port=8080)
```

### ayn.export_as_langserve(controller, metadata=None)

Export agent as LangServe compatible service

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]) – Optional agent metadata
* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)
* **Returns:**
  LangServe app

### Example

```pycon
>>> # Requires langserve - doctest: +SKIP
>>> controller = GenericController(...)
>>> app = export_as_langserve(controller)
```

### ayn.generate_chatgpt_action(controller, metadata, api_url)

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

### ayn.generate_claude_mcp_config(mcp_server, server_url, transport='sse')

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

| [`actions`](ayn.actions.html.md#module-ayn.actions)         | Custom actions for ChatGPT and Claude.      |
|-------------------------------------------------------------------------------------|---------------------------------------------|
| [`controllers`](ayn.controllers.html.md#module-ayn.controllers) | Agent controllers for invoking agents.      |
| [`core`](ayn.core.html.md#module-ayn.core)               | Core data models and configuration for AYN. |
| [`export`](ayn.export.html.md#module-ayn.export)           | Export agents as HTTP/REST services.        |
| [`mcp`](ayn.mcp.html.md#module-ayn.mcp)                 | Model Context Protocol support.             |
| [`registry`](ayn.registry.html.md#module-ayn.registry)       | Agent registry and search functionality.    |
| [`utils`](ayn.utils.html.md#module-ayn.utils)             | Convenience utility functions.              |
