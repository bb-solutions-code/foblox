"""Unit tests for the foblox `if` block."""

from __future__ import annotations

import importlib

from bbscript.core.registry import get_block

IfBlock = importlib.import_module("if.if").IfBlock


def test_if_registered() -> None:
    assert get_block("if") is IfBlock


def test_if_true_passthrough() -> None:
    assert IfBlock().run({"condition": True}, {}) is True


def test_if_false_passthrough() -> None:
    assert IfBlock().run({"condition": False}, {}) is False


def test_if_coerces_truthy_values() -> None:
    assert IfBlock().run({"condition": "x"}, {}) is True


def test_if_parses_false_string() -> None:
    assert IfBlock().run({"condition": "false"}, {}) is False
