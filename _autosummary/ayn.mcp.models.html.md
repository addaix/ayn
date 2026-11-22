# ayn.mcp.models

MCP data models.

### Classes

| [`MCPPrompt`](#ayn.mcp.models.MCPPrompt)(name, description[, arguments])       | MCP prompt template     |
|--------------------------------------------------------------------------------------------------|-------------------------|
| [`MCPResource`](#ayn.mcp.models.MCPResource)(uri, name[, mimeType, description]) | MCP resource definition |
| [`MCPTool`](#ayn.mcp.models.MCPTool)(name, description, input_schema[, ...]) | MCP tool definition     |

### *class* ayn.mcp.models.MCPPrompt(name, description, arguments=list())

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP prompt template

### Example

```pycon
>>> prompt = MCPPrompt(
...     name="summarize",
...     description="Summarize text",
...     arguments=[{"name": "text", "description": "Text to summarize", "required": True}]
... )
>>> prompt.name
'summarize'
```

#### to_dict()

Convert to MCP prompt format

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### *class* ayn.mcp.models.MCPResource(uri, name, mimeType='text/plain', description='')

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP resource definition

### Example

```pycon
>>> resource = MCPResource(
...     uri="file:///data.csv",
...     name="Dataset",
...     mimeType="text/csv"
... )
>>> resource.name
'Dataset'
```

#### to_dict()

Convert to MCP resource format

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)

### *class* ayn.mcp.models.MCPTool(name, description, input_schema, handler=None)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

MCP tool definition

### Example

```pycon
>>> tool = MCPTool(
...     name="search",
...     description="Search for information",
...     input_schema={"type": "object", "properties": {"query": {"type": "string"}}}
... )
>>> tool.name
'search'
```

#### to_dict()

Convert to MCP tool format

* **Return type:**
  [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)
