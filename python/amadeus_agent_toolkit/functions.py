import amadeus
from typing import List, Optional, Dict, Any
from .configuration import Context
import json


def search_flights(
    context: Context,
    client: amadeus.Client,
    origin_location_code: str,
    destination_location_code: str,
    departure_date: str,
    adults: int,
    max: int = 10,
    return_date: Optional[str] = None,
    children: Optional[int] = None,
    non_stop: Optional[bool] = None,
    currency_code: str = "INR",
) -> Dict[str, Any]:
    """Searches for the cheapest flights between two locations on a given date.

    Parameters:
        origin_location_code: IATA code of the departure city/airport (e.g., "MAD").
        destination_location_code: IATA code of the destination city/airport (e.g., "BOS").
        departure_date: The date of departure in YYYY-MM-DD format.
        adults: The number of adult passengers.
        max: maximum number of flight offers to return. If specified, the value should be greater than or equal to 1
        return_date: Optional return date in YYYY-MM-DD format for round trips.
        children: Optional number of children (2-11 years).
        non_stop: Optional boolean to filter for non-stop flights only.
        currency_code: The preferred currency for flight offers (default: "INR").

    Returns:
        A dictionary containing the flight offers or an error dictionary.
    """

    flight_search_data: Dict[str, Any] = {
        "originLocationCode": origin_location_code,
        "destinationLocationCode": destination_location_code,
        "departureDate": departure_date,
        "adults": adults,
        "max": max,
        "currencyCode": currency_code,
    }

    if return_date is not None:
        flight_search_data["returnDate"] = return_date
    if children is not None:
        flight_search_data["children"] = children
    if non_stop is not None:
        flight_search_data["nonStop"] = non_stop

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


def search_hotels(
    context: Context,
    client: amadeus.Client,
    city_code: str,
    ratings: Optional[int] = None,
    radius: Optional[int] = None,
    radiusUnit: Optional[str] = None,
) -> Dict[str, Any]:
    """Searches for the hotels between given a city code.

    Parameters:
        city_code: IATA code of the departure city/airport (e.g., "MAD")
        ratings: The ratings of the hotels (e.g., 5). Allowed values are 1, 2, 3, 4, 5.
                 5 is for top rated hotels.
        radius: The radius of the search (e.g., 100)
        radiusUnit: The unit of the radius (e.g., "KM")

    Returns:
        A list containing hotels or an error dictionary.
    """

    hotels_search_data: Dict[str, Any] = {
        "cityCode": city_code,
    }

    if ratings is not None:
        hotels_search_data["ratings"] = ratings
    if radius is not None:
        hotels_search_data["radius"] = radius
    if radiusUnit is not None:
        hotels_search_data["radiusUnit"] = radiusUnit

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


def get_hotels(
    context: Any,
    client: amadeus.Client,
    hotel_ids: List[str],
    check_in_date: str,
    check_out_date: str,
    adults: int,
) -> dict:
    """Retrieve hotel details, including availability,
       rooms, prices, and offer conditions.

    Parameters:
        context: The request context
                (not used in the function, but included for compatibility).
        client: The Amadeus API client instance.
        hotel_ids: A list of unique hotel IDs.
        check_in_date: Check-in date of the stay (hotel local date). Format YYYY-MM-DD.
        check_out_date: Check-out date of the stay (hotel local date). Format YYYY-MM-DD.
        adults: Number of adult guests (1-9) per room.

    Returns:
        A dictionary containing hotel details such as available rooms,
        prices, and offer conditions.
    """

    hotels_get_data: Dict[str, Any] = {
        "hotelIds": hotel_ids,
        "checkInDate": check_in_date,
        "checkOutDate": check_out_date,
        "adults": adults,
        "roomQuantity": 1,
    }

    print(json.dumps(hotels_get_data, indent=4))

    try:
        response = client.shopping.hotel_offers_search.get(
            **hotels_get_data)
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
