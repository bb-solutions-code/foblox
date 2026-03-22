"""Unit tests for the foblox `say` block."""

from __future__ import annotations

from bbscript.core.registry import get_block

from say.say import SayBlock


def test_say_registered() -> None:
    assert get_block("say") is SayBlock


def test_say_prints_and_passthrough_str(capsys) -> None:
    out = SayBlock().run({"input": "hello"}, {})
    assert out == "hello"
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


def test_say_passthrough_none(capsys) -> None:
    out = SayBlock().run({"input": None}, {})
    assert out is None
    captured = capsys.readouterr()
    assert captured.out == "None\n"


def test_say_passthrough_dict(capsys) -> None:
    value = {"a": 1}
    out = SayBlock().run({"input": value}, {})
    assert out is value
    captured = capsys.readouterr()
    assert captured.out.rstrip("\n") == str(value)
