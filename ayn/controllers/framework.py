"""Framework-specific controller implementations."""

from __future__ import annotations

from .generic import GenericController


class CrewAIController(GenericController):
    """Controller for CrewAI agents

    Not implemented yet: today this behaves exactly like :class:`GenericController`
    (it echoes its input) and does not run a CrewAI agent.
    See AYN_IMPLEMENTATION_ROADMAP.md for details
    """

    pass


class LangChainController(GenericController):
    """Controller for LangChain agents

    Not implemented yet: today this behaves exactly like :class:`GenericController`
    (it echoes its input) and does not run a LangChain agent.
    See AYN_IMPLEMENTATION_ROADMAP.md for details
    """

    pass


class AutoGenController(GenericController):
    """Controller for AutoGen agents

    Not implemented yet: today this behaves exactly like :class:`GenericController`
    (it echoes its input) and does not run an AutoGen agent.
    See AYN_IMPLEMENTATION_ROADMAP.md for details
    """

    pass
