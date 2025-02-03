from typing import Optional
from pydantic import BaseModel, Field


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


class SearchHotels(BaseModel):
    """Schema for `search_hotels` operation."""

    city_code: str = Field(
        ...,
        description="Destination city code or airport code. In case of city code , the search will be done around the city center. Available codes can be found in IATA table codes (3 chars IATA Code). Example PAR, BLR",
    )


class GetHotels(BaseModel):
    """Schema for `get_hotels` operation."""

    hotel_ids: list[str] = Field(
        ...,
        description="A list of unique hotel ID, these IDs are returned in SearchHotels usually."
    )

    check_in_date: str = Field(
        ...,
        description="Check-in date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is the present date (no dates in the past). If not present, the default value will be today's date in the GMT",
    )

    check_out_date: str = Field(
        ...,
        description="Check-out date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is checkInDate+1. If not present, it will default to checkInDate +1.",
    )

    adults: int = Field(
        ...,
        description="Number of adult guests (1-9) per room.",
    )
