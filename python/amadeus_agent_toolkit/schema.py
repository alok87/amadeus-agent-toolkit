from typing import Optional
from pydantic import BaseModel, Field


class SearchHotels(BaseModel):
    """Schema for `search_hotels` operation."""

    city_code: str = Field(
        ...,
        description="Destination city code or airport code. In case of city code , the search will be done around the city center. Available codes can be found in IATA table codes (3 chars IATA Code). Example PAR, BLR",
    )


class SearchFlights(BaseModel):
    """Schema for the `search_flights` operation."""

    origin_location_code: str = Field(
        ...,
        description="origin_location_code – the City/Airport IATA code from which the flight will depart. 'BLR', for example for Bangalore.",
    )

    destination_location_code: str = Field(
        ...,
        description="destination_location_code – the City/Airport IATA code to which the flight is going. 'GOI', for example for Goa.",
    )

    departure_date: str = Field(
        ...,
        description="the date on which to fly out, in YYYY-MM-DD format",
    )

    adults: str = Field(
        ...,
        description="the number of adult passengers with age 12 or older",
    )
