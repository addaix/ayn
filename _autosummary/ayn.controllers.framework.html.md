# ayn.controllers.framework

Framework-specific controller implementations.

### Classes

| [`AutoGenController`](#ayn.controllers.framework.AutoGenController)(metadata, config)   | Controller for AutoGen agents   |
|----------------------------------------------------------------------------------------|---------------------------------|
| [`CrewAIController`](#ayn.controllers.framework.CrewAIController)(metadata, config)    | Controller for CrewAI agents    |
| [`LangChainController`](#ayn.controllers.framework.LangChainController)(metadata, config) | Controller for LangChain agents |

### *class* ayn.controllers.framework.AutoGenController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for AutoGen agents

Not implemented yet: today this behaves exactly like `GenericController`
(it echoes its input) and does not run an AutoGen agent.
See AYN_IMPLEMENTATION_ROADMAP.md for details

### *class* ayn.controllers.framework.CrewAIController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for CrewAI agents

Not implemented yet: today this behaves exactly like `GenericController`
(it echoes its input) and does not run a CrewAI agent.
See AYN_IMPLEMENTATION_ROADMAP.md for details

### *class* ayn.controllers.framework.LangChainController(metadata, config)

Bases: [`GenericController`](ayn.controllers.generic.html.md#ayn.controllers.generic.GenericController)

Controller for LangChain agents

Not implemented yet: today this behaves exactly like `GenericController`
(it echoes its input) and does not run a LangChain agent.
See AYN_IMPLEMENTATION_ROADMAP.md for details
