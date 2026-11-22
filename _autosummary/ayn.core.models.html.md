# ayn.core.models

Core data models for agents.

### Classes

| [`AgentFramework`](#ayn.core.models.AgentFramework)(\*values)                    | Supported agent frameworks   |
|----------------------------------------------------------------------------------------------|------------------------------|
| [`AgentMetadata`](#ayn.core.models.AgentMetadata)(name, description, framework) | Metadata for an agent        |
| [`AgentModality`](#ayn.core.models.AgentModality)(\*values)                     | Agent modalities             |

### *class* ayn.core.models.AgentFramework(\*values)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Supported agent frameworks

### *class* ayn.core.models.AgentMetadata(name, description, framework, source='', tags=list(), modality=AgentModality.TEXT, version='0.1.0', author='', license='', dependencies=list(), capabilities=list())

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
  [`AgentMetadata`](#ayn.core.models.AgentMetadata)

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

### *class* ayn.core.models.AgentModality(\*values)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Agent modalities
