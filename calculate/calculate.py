"""Calculate block: binary arithmetic on two numbers."""

from __future__ import annotations

from typing import Any, Dict, List

from bbscript.core.block_base import Block, BlockArgument, BlockOutput
from bbscript.core.registry import register_block


@register_block("calculate")
class CalculateBlock(Block):
    @classmethod
    def arguments(cls) -> List[BlockArgument]:
        return [
            BlockArgument(
                name="a",
                type="number",
                description="First operand.",
            ),
            BlockArgument(
                name="b",
                type="number",
                description="Second operand.",
            ),
            BlockArgument(
                name="operation",
                type="option(+, -, *, /, pow)",
                description="Arithmetic operation: +, -, *, /, or pow.",
            ),
        ]

    @classmethod
    def output(cls) -> BlockOutput:
        return BlockOutput(name="output", type="number")

    def run(self, args: Dict[str, Any], context: Dict[str, Any]) -> Any:
        a = float(args["a"])
        b = float(args["b"])
        op = args["operation"]
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a / b
        if op == "pow":
            return a**b
        raise ValueError(f"Unsupported operation: {op!r}")
