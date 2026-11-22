# ayn.controllers

Agent controllers for invoking agents.

### Classes

| [`AgentController`](#ayn.controllers.AgentController)(\*args, \*\*kwargs)   | Standard protocol for agent controllers   |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| [`BaseAgentController`](#ayn.controllers.BaseAgentController)(config)           | Base class for agent controllers          |
| [`GenericController`](#ayn.controllers.GenericController)(metadata, config)   | Generic controller for custom agents      |
| [`CrewAIController`](#ayn.controllers.CrewAIController)(metadata, config)    | Controller for CrewAI agents              |
| [`LangChainController`](#ayn.controllers.LangChainController)(metadata, config) | Controller for LangChain agents           |
| [`AutoGenController`](#ayn.controllers.AutoGenController)(metadata, config)   | Controller for AutoGen agents             |

### *class* ayn.controllers.AgentController(\*args, \*\*kwargs)

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

### *class* ayn.controllers.AutoGenController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for AutoGen agents

### *class* ayn.controllers.BaseAgentController(config)

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

### *class* ayn.controllers.CrewAIController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for CrewAI agents

### *class* ayn.controllers.GenericController(metadata, config)

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

### *class* ayn.controllers.LangChainController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for LangChain agents

### Modules

| [`base`](ayn.controllers.base.html.md#module-ayn.controllers.base)           | Base controller protocol and abstract class.   |
|---------------------------------------------------------------------------------------------|------------------------------------------------|
| [`framework`](ayn.controllers.framework.html.md#module-ayn.controllers.framework) | Framework-specific controller implementations. |
| [`generic`](ayn.controllers.generic.html.md#module-ayn.controllers.generic)     | Generic controller for custom agents.          |
