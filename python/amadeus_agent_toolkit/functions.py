import amadeus
from typing import Optional, Dict, Any
from .configuration import Context
import json


def search_hotels(
    context: Context,
    client: amadeus.Client,
    city_code: str,
) -> dict:
    """Searches for the hotels between given a city code.

    Parameters:
        city_code: IATA code of the departure city/airport (e.g., "MAD").

    Returns:
        A list containing hotels or an error dictionary.
    """

    hotels_search_data: Dict[str, Any] = {
        "cityCode": city_code,
    }

    print(json.dumps(hotels_search_data, indent=4))

    try:
        response = client.reference_data.locations.hotels.by_city.get(
            **hotels_search_data)
        return response.data
    except amadeus.ResponseError as e:
        print(f"Amadeus Error: {e}")
        return {
            "error": str(e),
            "type": "AmadeusError"
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "error": "An unexpected error occurred",
            "type": "UnexpectedError"
        }


def search_flights(
    context: Context,
    client: amadeus.Client,
    origin_location_code: str,
    destination_location_code: str,
    departure_date: str,
    adults: int,
) -> dict:
    """Searches for the cheapest flights between two locations on a given date.

    Parameters:
        origin_location_code: IATA code of the departure city/airport (e.g., "MAD").
        destination_location_code: IATA code of the destination city/airport (e.g., "BOS").
        departure_date: The date of departure in YYYY-MM-DD format.
        adults: The number of adult passengers.

    Returns:
        A dictionary containing the flight offers or an error dictionary.
    """

    flight_search_data: Dict[str, Any] = {
        "originLocationCode": origin_location_code,
        "destinationLocationCode": destination_location_code,
        "departureDate": departure_date,
        "adults": adults,
    }

    print(json.dumps(flight_search_data, indent=4))

    try:
        response = client.shopping.flight_offers_search.get(**flight_search_data)
        return response.data
    except amadeus.ResponseError as e:
        print(f"Amadeus Error: {e}")
        return {
            "error": str(e),
            "type": "AmadeusError"
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "error": "An unexpected error occurred",
            "type": "UnexpectedError"
        }
