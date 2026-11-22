# ayn.utils

Convenience utility functions.

### Functions

| [`create_agent_from_registry`](#ayn.utils.create_agent_from_registry)(registry, query)       | Search registry and create agent controller   |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [`export_agent_full_stack`](#ayn.utils.export_agent_full_stack)(controller, metadata, \*) | Export agent with all integrations            |

### ayn.utils.create_agent_from_registry(registry, query, config=None)

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

### ayn.utils.export_agent_full_stack(controller, metadata, , api_host='0.0.0.0', api_port=8000, export_fastapi=True, export_mcp=True, export_chatgpt=True, mcp_tools=None)

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
