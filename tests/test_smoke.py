"""Smoke tests: the public API imports and the core models behave."""

from ayn import AgentFramework, AgentMetadata


def test_metadata_to_dict_roundtrip_keeps_name_and_description():
    meta = AgentMetadata(
        name="demo", description="a demo agent", framework=AgentFramework.CREWAI
    )
    d = meta.to_dict()
    assert d["name"] == "demo"
    assert d["description"] == "a demo agent"


def test_metadata_defaults_are_independent_per_instance():
    a = AgentMetadata(name="a", description="x", framework=AgentFramework.CREWAI)
    b = AgentMetadata(name="b", description="y", framework=AgentFramework.CREWAI)
    a.tags.append("t")
    assert b.tags == []
