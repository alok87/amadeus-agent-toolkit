"""
This tool allows agents to interact with the Amadeus API.
"""

from __future__ import annotations

from typing import Any, Optional, Type

from langchain.tools import BaseTool
from pydantic import BaseModel

from ..api import AmadeusAPI


class AmadeusTool(BaseTool):
    """Tool for interacting with the Amadeus API."""

    amadeus_api: AmadeusAPI
    method: str
    name: str = ""
    description: str = ""
    args_schema: Optional[Type[BaseModel]] = None

    def _run(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        """Use the amadeus API to run an operation."""
        return self.amadeus_api.run(self.method, *args, **kwargs)
