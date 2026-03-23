"""If block: normalize a condition into a strict boolean value."""

from __future__ import annotations

from typing import Any, Dict, List

from bbscript.core.block_base import Block, BlockArgument, BlockOutput
from bbscript.core.registry import register_block


@register_block("if")
class IfBlock(Block):
    @classmethod
    def arguments(cls) -> List[BlockArgument]:
        return [
            BlockArgument(
                name="condition",
                type="any",
                description="Condition value to evaluate as boolean.",
            )
        ]

    @classmethod
    def output(cls) -> BlockOutput:
        return BlockOutput(name="output", type="boolean")

    def run(self, args: Dict[str, Any], context: Dict[str, Any]) -> Any:
        value = args.get("condition")
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"true", "1", "yes", "on"}:
                return True
            if normalized in {"false", "0", "no", "off", ""}:
                return False
        return bool(value)
