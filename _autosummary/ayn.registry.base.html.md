# ayn.registry.base

Agent registry implementation.

### Classes

| [`AgentRegistry`](#ayn.registry.base.AgentRegistry)([searchers, cache_dir])   | Unified registry for searching and managing agents   |
|------------------------------------------------------------------------------------------|------------------------------------------------------|

### *class* ayn.registry.base.AgentRegistry(searchers=None, cache_dir=None)

Bases: [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]

Unified registry for searching and managing agents

Aggregates results from multiple sources and provides a dict-like interface.

Pass `searchers=[]` for a local-only registry, and a `cache_dir` to keep the
cache out of `~/.ayn/registry`.

### Example

```pycon
>>> import tempfile
>>> registry = AgentRegistry(searchers=[], cache_dir=tempfile.mkdtemp())
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
>>> import tempfile
>>> registry = AgentRegistry(searchers=[], cache_dir=tempfile.mkdtemp())
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
