# ayn.actions.chatgpt

ChatGPT custom action generation.

### Functions

| [`generate_chatgpt_action`](#ayn.actions.chatgpt.generate_chatgpt_action)(controller, ...)   | Generate ChatGPT custom action configuration   |
|---------------------------------------------------------------------------------------------|------------------------------------------------|

### ayn.actions.chatgpt.generate_chatgpt_action(controller, metadata, api_url)

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
