from typing import Dict, List

from .prompts import SEARCH_FLIGHTS_PROMPT
from .schema import SearchFlights

tools: List[Dict] = [
    {
        "method": "search_flights",
        "name": "Search Flights",
        "description": SEARCH_FLIGHTS_PROMPT,
        "args_schema": SearchFlights,
        "actions": {
            "flights": {
                "search": True,
            }
        },
    }
]
