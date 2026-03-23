"""Unit tests for the foblox `switch` block."""

from __future__ import annotations

from bbscript.core.registry import get_block

from switch.switch import SwitchBlock


def test_switch_registered() -> None:
    assert get_block("switch") is SwitchBlock


def test_switch_returns_input_value() -> None:
    assert SwitchBlock().run({"value": "pro"}, {}) == "pro"


def test_switch_returns_none_when_missing() -> None:
    assert SwitchBlock().run({}, {}) is None
