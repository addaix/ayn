# ayn.export

Export agents as HTTP/REST services.

### Functions

| [`export_as_fastapi`](#ayn.export.export_as_fastapi)(controller[, metadata, ...])   | Export agent controller as FastAPI service   |
|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| [`export_as_langserve`](#ayn.export.export_as_langserve)(controller[, metadata])      | Export agent as LangServe compatible service |

### ayn.export.export_as_fastapi(controller, metadata=None, host='0.0.0.0', port=8000)

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

### ayn.export.export_as_langserve(controller, metadata=None)

Export agent as LangServe compatible service

* **Parameters:**
  * **controller** ([`AgentController`](ayn.controllers.base.html.md#ayn.controllers.base.AgentController)) – Agent controller
  * **metadata** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`AgentMetadata`](ayn.core.models.html.md#ayn.core.models.AgentMetadata)]) – Optional agent metadata
* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)
* **Returns:**
  LangServe app

### Example

```pycon
>>> # Requires langserve - doctest: +SKIP
>>> controller = GenericController(...)
>>> app = export_as_langserve(controller)
```

### Modules

| [`fastapi_export`](ayn.export.fastapi_export.html.md#module-ayn.export.fastapi_export)     | FastAPI export functionality.   |
|------------------------------------------------------------------------------------------------------|---------------------------------|
| [`langserve_export`](ayn.export.langserve_export.html.md#module-ayn.export.langserve_export) | LangServe export functionality. |
