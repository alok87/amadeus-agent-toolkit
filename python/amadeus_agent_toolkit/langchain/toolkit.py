"""Amadeus Agent Toolkit."""

from typing import List, Optional

from pydantic import PrivateAttr

from ..api import AmadeusAPI
from ..configuration import Configuration, is_tool_allowed
from ..tools import tools
from .tool import AmadeusTool


class AmadeusAgentToolkit:
    _tools: List["AmadeusTool"] = PrivateAttr(default_factory=list)

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        configuration: Optional[Configuration] = None
    ):
        super().__init__()

        context = configuration.get("context") if configuration else None

        amadeus_api = AmadeusAPI(
            client_id=client_id, client_secret=client_secret, context=context)

        filtered_tools = [
            tool for tool in tools if is_tool_allowed(tool, configuration)
        ]

        self._tools = [
            AmadeusTool(
                name=tool["method"],
                description=tool["description"],
                method=tool["method"],
                amadeus_api=amadeus_api,
                args_schema=tool.get("args_schema", None),
            )
            for tool in filtered_tools
        ]

    def get_tools(self) -> List["AmadeusTool"]:
        """Get the tools in the toolkit."""
        return self._tools
