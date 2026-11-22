# ayn.controllers.generic

Generic controller for custom agents.

### Classes

| [`GenericController`](#ayn.controllers.generic.GenericController)(metadata, config)   | Generic controller for custom agents   |
|----------------------------------------------------------------------------------------|----------------------------------------|

### *class* ayn.controllers.generic.GenericController(metadata, config)

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
