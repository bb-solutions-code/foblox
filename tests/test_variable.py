"""Unit tests for the foblox `variable` block."""

from __future__ import annotations

from bbscript.core.registry import get_block

from variable.variable import VariableBlock


def test_variable_registered() -> None:
    assert get_block("variable") is VariableBlock


def test_variable_passthrough_str() -> None:
    out = VariableBlock().run({"value": "hello"}, {})
    assert out == "hello"


def test_variable_passthrough_none() -> None:
    out = VariableBlock().run({"value": None}, {})
    assert out is None


def test_variable_passthrough_dict() -> None:
    value = {"a": 1}
    out = VariableBlock().run({"value": value}, {})
    assert out is value


def test_variable_missing_value() -> None:
    out = VariableBlock().run({}, {})
    assert out is None
