from typing import Dict, List, Any

from .prompts import SEARCH_FLIGHTS_PROMPT, \
    SEARCH_HOTELS_PROMPT, GET_HOTELS_PROMPT
from .schema import SearchHotels, SearchFlights, GetHotels


tools: List[Dict[str, Any]] = [
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
    {
        "method": "get_hotels",
        "name": "Get Hotels",
        "description": GET_HOTELS_PROMPT,
        "args_schema": GetHotels,
        "actions": {
            "hotels": {
                "get": True,
            }
        },
    },
]
