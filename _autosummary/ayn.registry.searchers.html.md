# ayn.registry.searchers

Agent searcher implementations.

### Classes

| [`AgentSearcher`](#ayn.registry.searchers.AgentSearcher)(\*args, \*\*kwargs)    | Protocol for agent search implementations   |
|---------------------------------------------------------------------------------------|---------------------------------------------|
| [`AwesomeListSearcher`](#ayn.registry.searchers.AwesomeListSearcher)()                | Parse and search awesome lists for agents   |
| [`GitHubAgentSearcher`](#ayn.registry.searchers.GitHubAgentSearcher)([github_token])  | Search for agents in GitHub repositories    |
| [`HuggingFaceAgentSearcher`](#ayn.registry.searchers.HuggingFaceAgentSearcher)([hf_token]) | Search for agents on Hugging Face           |

### *class* ayn.registry.searchers.AgentSearcher(\*args, \*\*kwargs)

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

### *class* ayn.registry.searchers.AwesomeListSearcher

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

### *class* ayn.registry.searchers.GitHubAgentSearcher(github_token=None)

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

### *class* ayn.registry.searchers.HuggingFaceAgentSearcher(hf_token=None)

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
