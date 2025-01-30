"""Abstraction above Amadeus."""

from __future__ import annotations

import json
import os
from typing import Optional

import amadeus
from pydantic import BaseModel

from .configuration import Context
from .functions import search_flights


class AmadeusAPI(BaseModel):
    """ "Wrapper for Amadeus API"""

    _context: Context
    _client: amadeus.Client

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        context: Optional[Context]):

        super().__init__()

        self._context = context if context is not None else Context()
        self._client = amadeus.Client(
            client_id=client_id,
            client_secret=client_secret,
        )

    def run(self, method: str, *args, **kwargs) -> str:
        if method == "search_flights":
            return json.dumps(
                search_flights(
                    self._context,
                    self._client,
                    *args,
                    **kwargs
                )
            )
        else:
            raise ValueError("Invalid method " + method)
