# ayn.core

Core data models and configuration for AYN.

### Classes

| [`AgentFramework`](#ayn.core.AgentFramework)(\*values)                    | Supported agent frameworks          |
|----------------------------------------------------------------------------------------------|-------------------------------------|
| [`AgentModality`](#ayn.core.AgentModality)(\*values)                     | Agent modalities                    |
| [`AgentMetadata`](#ayn.core.AgentMetadata)(name, description, framework) | Metadata for an agent               |
| [`ControllerConfig`](#ayn.core.ControllerConfig)([model, temperature, ...]) | Configuration for agent controllers |

### *class* ayn.core.AgentFramework(\*values)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Supported agent frameworks

### *class* ayn.core.AgentMetadata(name, description, framework, source='', tags=list(), modality=AgentModality.TEXT, version='0.1.0', author='', license='', dependencies=list(), capabilities=list())

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

### *class* ayn.core.AgentModality(\*values)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Agent modalities

### *class* ayn.core.ControllerConfig(model='gpt-4', temperature=0.7, max_tokens=1000, timeout=60, retry_count=3, api_key=None, additional_params=dict())

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

### Modules

| [`config`](ayn.core.config.html.md#module-ayn.core.config)   | Configuration for agent controllers.   |
|----------------------------------------------------------------------------------|----------------------------------------|
| [`models`](ayn.core.models.html.md#module-ayn.core.models)   | Core data models for agents.           |
