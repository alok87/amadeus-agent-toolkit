SEARCH_FLIGHTS_PROMPT = """
This tool will search for the cheapest flight offers using the Amadeus Flight Offers Search API.

It takes the following arguments:

- origin_location_code (str): The IATA code of the departure city/airport (e.g., "MAD" for Madrid).
- destination_location_code (str): The IATA code of the arrival city/airport (e.g., "BOS" for Boston).
- departure_date (str): The departure date in YYYY-MM-DD format (e.g., "2024-03-15").
- adults (int): The number of adult passengers (12 years or older).

Example usage:

To find the cheapest flights from Madrid (MAD) to Boston (BOS) on March 15, 2024, for 2 adults, you would provide the following arguments:

origin_location_Code="MAD"
destination_location_code="BOS"
departure_date="2024-03-15"
adults=2

This tool returns a list of flight offers, sorted by price.  It may raise an error (amadeus.ResponseError) if the request fails.
"""

SEARCH_HOTELS_PROMPT = """
This tool will search for hotels in a city

It takes the following arguments:

- city_code (str): The IATA code for the city where the hotel needs to be searched. (e.g., BLR)

Example usage:

To find the most relevant hotel based on current context, you would provide the following arguments:

city_code="BLR"

This tool returns the list of hotels with that city code
"""

GET_HOTELS_PROMPT = """
This tool retrieves detailed information about hotels based on a list of hotel IDs.

It takes the following arguments:
- hotel_ids (list[str]): A list of unique hotel IDs. These IDs are typically obtained from the hotel search results.

Example usage:

To retrieve details for specific hotels, you would provide the following arguments:

hotel_ids=["12345", "67890"]

This tool returns information such as hotel offers, available rooms, pricing, offer conditions, and other relevant details.
"""
