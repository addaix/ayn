# ayn.export.fastapi_export

FastAPI export functionality.

### Functions

| [`export_as_fastapi`](#ayn.export.fastapi_export.export_as_fastapi)(controller[, metadata, ...])   | Export agent controller as FastAPI service   |
|---------------------------------------------------------------------------------------------------|----------------------------------------------|

### ayn.export.fastapi_export.export_as_fastapi(controller, metadata=None, host='0.0.0.0', port=8000)

Export agent controller as FastAPI service

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]) – Optional agent metadata
  * **host** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Host to bind to
  * **port** ([`int`](https://docs.python.org/3/builtins/functions.html#int)) – Port to bind to

### Example

```pycon
>>> # This would start a server - doctest: +SKIP
>>> controller = GenericController(...)
>>> export_as_fastapi(controller, port=8080)
```
