"""Switch block: return selector value for control-flow routing."""

from __future__ import annotations

from typing import Any, Dict, List

from bbscript.core.block_base import Block, BlockArgument, BlockOutput
from bbscript.core.registry import register_block


@register_block("switch")
class SwitchBlock(Block):
    @classmethod
    def arguments(cls) -> List[BlockArgument]:
        return [
            BlockArgument(
                name="value",
                type="any",
                description="Selector value used by control links.",
            )
        ]

    @classmethod
    def output(cls) -> BlockOutput:
        return BlockOutput(name="output", type="any")

    def run(self, args: Dict[str, Any], context: Dict[str, Any]) -> Any:
        return args.get("value")
