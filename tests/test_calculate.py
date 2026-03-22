"""Unit tests for the foblox `calculate` block."""

from __future__ import annotations

import pytest

from bbscript.core.registry import get_block

from calculate.calculate import CalculateBlock


def test_calculate_registered() -> None:
    assert get_block("calculate") is CalculateBlock


def test_calculate_add() -> None:
    out = CalculateBlock().run({"a": 2, "b": 3, "operation": "+"}, {})
    assert out == 5.0


def test_calculate_subtract() -> None:
    out = CalculateBlock().run({"a": 10, "b": 4, "operation": "-"}, {})
    assert out == 6.0


def test_calculate_multiply() -> None:
    out = CalculateBlock().run({"a": 2, "b": 3, "operation": "*"}, {})
    assert out == 6.0


def test_calculate_divide() -> None:
    out = CalculateBlock().run({"a": 10, "b": 4, "operation": "/"}, {})
    assert out == 2.5


def test_calculate_pow() -> None:
    out = CalculateBlock().run({"a": 2, "b": 3, "operation": "pow"}, {})
    assert out == 8.0


def test_calculate_unknown_operation() -> None:
    with pytest.raises(ValueError, match="Unsupported operation"):
        CalculateBlock().run({"a": 1, "b": 2, "operation": "%"}, {})


def test_calculate_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        CalculateBlock().run({"a": 1, "b": 0, "operation": "/"}, {})
