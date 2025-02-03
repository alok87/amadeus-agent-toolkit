from typing import Dict, List

from .prompts import SEARCH_FLIGHTS_PROMPT, SEARCH_HOTELS_PROMPT
from .schema import SearchHotels, SearchFlights

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
    },
    {
        "method": "search_hotels",
        "name": "Search Hotels",
        "description": SEARCH_HOTELS_PROMPT,
        "args_schema": SearchHotels,
        "actions": {
            "hotels": {
                "search": True,
            }
        },
    },
]
