"""Variable block: pass a value through to execution context under the instance output name."""

from __future__ import annotations

from typing import Any, Dict, List

from bbscript.core.block_base import Block, BlockArgument, BlockOutput
from bbscript.core.registry import register_block


@register_block("variable")
class VariableBlock(Block):
    @classmethod
    def arguments(cls) -> List[BlockArgument]:
        return [
            BlockArgument(
                name="value",
                type="any",
                description="Value to store and expose as this block's output.",
            )
        ]

    @classmethod
    def output(cls) -> BlockOutput:
        return BlockOutput(name="output", type="any")

    def run(self, args: Dict[str, Any], context: Dict[str, Any]) -> Any:
        return args.get("value")
