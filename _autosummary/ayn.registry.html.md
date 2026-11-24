# ayn.registry

Agent registry and search functionality.

### Classes

| [`AgentSearcher`](#ayn.registry.AgentSearcher)(\*args, \*\*kwargs)     | Protocol for agent search implementations          |
|----------------------------------------------------------------------------------------|----------------------------------------------------|
| [`GitHubAgentSearcher`](#ayn.registry.GitHubAgentSearcher)([github_token])   | Search for agents in GitHub repositories           |
| [`HuggingFaceAgentSearcher`](#ayn.registry.HuggingFaceAgentSearcher)([hf_token])  | Search for agents on Hugging Face                  |
| [`AwesomeListSearcher`](#ayn.registry.AwesomeListSearcher)()                 | Parse and search awesome lists for agents          |
| [`AgentRegistry`](#ayn.registry.AgentRegistry)([searchers, cache_dir]) | Unified registry for searching and managing agents |

### *class* ayn.registry.AgentRegistry(searchers=None, cache_dir=None)

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

### *class* ayn.registry.AgentSearcher(\*args, \*\*kwargs)

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

### *class* ayn.registry.AwesomeListSearcher

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

### *class* ayn.registry.GitHubAgentSearcher(github_token=None)

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

### *class* ayn.registry.HuggingFaceAgentSearcher(hf_token=None)

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

### Modules

| [`base`](ayn.registry.base.html.md#module-ayn.registry.base)           | Agent registry implementation.   |
|------------------------------------------------------------------------------------------|----------------------------------|
| [`searchers`](ayn.registry.searchers.html.md#module-ayn.registry.searchers) | Agent searcher implementations.  |
