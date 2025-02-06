SEARCH_FLIGHTS_PROMPT = """
This tool searches for the cheapest flights using Amadeus Flight Offers Search API.

Arguments:
- origin_location_code: IATA code of departure city (e.g., "MAD")
- destination_location_code: IATA code of arrival city (e.g., "BOS")
- departure_date: Date in YYYY-MM-DD format
- adults: Number of adult passengers (12+ years)
- return_date (optional): Return date in YYYY-MM-DD format
- children (optional): Number of children (2-11 years)
- non_stop (optional): If true, only non-stop flights
- currency_code (optional): Currency for prices (default: "INR")
- max (optional): Max flight offers to return (default: 10)

Example:
origin_location_code="MAD"
destination_location_code="BOS"
departure_date="2024-03-15"
return_date="2024-03-22"
adults=2
children=1
non_stop=true

Returns flight offers sorted by price. May raise amadeus.ResponseError on failure.
"""

SEARCH_HOTELS_PROMPT = """
This tool will search for hotels in a city

It takes the following arguments:

- city_code (str): The IATA code for the city where the hotel needs to be searched. (e.g., BLR)
- ratings (int, optional): Filter hotels by their rating. Allowed values are 1-5, where 5 represents top rated hotels.
- radius (int, optional): The radius within which to search for hotels from the city center.
- radiusUnit (str, optional): The unit of measurement for the radius (e.g., "KM").

Example usage:

To find hotels in Bangalore with a 5-star rating within 10 KM of the city center:

city_code="BLR"
ratings=5
radius=10
radiusUnit="KM"

This tool returns the list of hotels matching the specified criteria
"""

GET_HOTELS_PROMPT = """
This tool retrieves detailed information about hotels based on a list of hotel IDs.

It takes the following arguments:
- hotel_ids (list[str]): A list of unique hotel IDs. These IDs are typically obtained from the hotel search results.
- check_in_date (str): Check-in date of the stay (hotel local date). Format YYYY-MM-DD.
- check_out_date (str): Check-out date of the stay (hotel local date). Format YYYY-MM-DD.
- adults (int): Number of adult guests (1-9) per room.

Example usage:

To retrieve details for specific hotels, you would provide the following arguments:

hotel_ids = ["12345", "67890"]
check_in_date = "2025-03-15"
check_out_date = "2025-03-20"
adults = 2

This tool returns information such as hotel offers, available rooms, pricing, offer conditions, and other relevant details.
"""
