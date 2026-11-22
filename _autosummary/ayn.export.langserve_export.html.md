# ayn.export.langserve_export

LangServe export functionality.

### Functions

| [`export_as_langserve`](#ayn.export.langserve_export.export_as_langserve)(controller[, metadata])   | Export agent as LangServe compatible service   |
|------------------------------------------------------------------------------------------------|------------------------------------------------|

### ayn.export.langserve_export.export_as_langserve(controller, metadata=None)

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
