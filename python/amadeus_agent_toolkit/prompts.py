SEARCH_FLIGHTS_PROMPT = """
This tool will search for the cheapest flight offers using the Amadeus Flight Offers Search API.

It takes the following arguments:

- origin_location_code (str): The IATA code of the departure city/airport (e.g., "MAD" for Madrid).
- destination_location_code (str): The IATA code of the arrival city/airport (e.g., "BOS" for Boston).
- departure_date (str): The departure date in YYYY-MM-DD format (e.g., "2024-03-15").
- adults (int): The number of adult passengers (12 years or older).
- return_date (str, optional): The return date in YYYY-MM-DD format for round trips.
- children (int, optional): The number of children passengers (2-11 years).
- non_stop (bool, optional): If true, return only non-stop flights.
- currency_code (str, optional): The preferred currency for flight offers (default: "INR").
- max (int, optional): Maximum number of flight offers to return (default: 10).

Example usage:

To find the cheapest round-trip flights from Madrid (MAD) to Boston (BOS) on March 15, 2024, returning March 22, 2024, for 2 adults and 1 child, with non-stop flights only:

origin_location_code="MAD"
destination_location_code="BOS"
departure_date="2024-03-15"
return_date="2024-03-22"
adults=2
children=1
non_stop=true
currency_code="INR"
max=10

This tool returns a list of flight offers, sorted by price. It may raise an error (amadeus.ResponseError) if the request fails.
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
