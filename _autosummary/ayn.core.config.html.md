# ayn.core.config

Configuration for agent controllers.

### Classes

| [`ControllerConfig`](#ayn.core.config.ControllerConfig)([model, temperature, ...])   | Configuration for agent controllers   |
|------------------------------------------------------------------------------------------------|---------------------------------------|

### *class* ayn.core.config.ControllerConfig(model='gpt-4', temperature=0.7, max_tokens=1000, timeout=60, retry_count=3, api_key=None, additional_params=dict())

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
