"""Declared stubs must say so instead of returning empty results (addaix/ayn#5)."""

import pytest

from ayn import (
    AgentFramework,
    AgentMetadata,
    AgentRegistry,
    AwesomeListSearcher,
    GitHubAgentSearcher,
    HuggingFaceAgentSearcher,
)


@pytest.mark.parametrize(
    "searcher",
    [GitHubAgentSearcher(), HuggingFaceAgentSearcher(), AwesomeListSearcher()],
)
def test_unimplemented_searchers_raise(searcher):
    with pytest.raises(NotImplementedError):
        list(searcher.search("anything"))


def test_registry_search_warns_and_still_finds_local_agents(tmp_path):
    registry = AgentRegistry(cache_dir=str(tmp_path))  # not the user's ~/.ayn cache
    meta = AgentMetadata(
        name="mine", description="local agent", framework=AgentFramework.CUSTOM
    )
    registry["mine"] = meta
    with pytest.warns(UserWarning, match="not implemented"):
        found = registry.search("mine")
        none = registry.search("zzz-nothing-matches")
    assert [m.name for m in found] == ["mine"]
    assert none == []
