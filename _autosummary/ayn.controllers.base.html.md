# ayn.controllers.base

Base controller protocol and abstract class.

### Classes

| [`AgentController`](#ayn.controllers.base.AgentController)(\*args, \*\*kwargs)   | Standard protocol for agent controllers   |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| [`BaseAgentController`](#ayn.controllers.base.BaseAgentController)(config)           | Base class for agent controllers          |

### *class* ayn.controllers.base.AgentController(\*args, \*\*kwargs)

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

### *class* ayn.controllers.base.BaseAgentController(config)

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
  [`BaseAgentController`](#ayn.controllers.base.BaseAgentController)

#### *abstractmethod* invoke(input_data, \*\*kwargs)

Invoke the agent - must be implemented by subclasses

* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)

#### stream(input_data, \*\*kwargs)

Default streaming yields single result

* **Return type:**
  [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]
