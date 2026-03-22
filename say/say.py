"""Say block: print input to the console and pass it through unchanged."""

from __future__ import annotations

from typing import Any, Dict, List

from bbscript.core.block_base import Block, BlockArgument
from bbscript.core.registry import register_block


@register_block("say")
class SayBlock(Block):
    @classmethod
    def arguments(cls) -> List[BlockArgument]:
        return [
            BlockArgument(
                name="input",
                type="any",
                description="Value to print and pass through.",
            )
        ]

    def run(self, args: Dict[str, Any], context: Dict[str, Any]) -> Any:
        value = args.get("input")
        print(value)
        return value
