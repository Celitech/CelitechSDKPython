from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class Destinations(BaseModel):
    """Destinations

    :param name: Name of the destination
    :type name: str
    :param destination: ISO3 representation of the destination
    :type destination: str
    :param destination_iso2: ISO2 representation of the destination
    :type destination_iso2: str
    :param supported_countries: This array indicates the geographical area covered by a specific destination. If the destination represents a single country, the array will include that country. However, if the destination represents a broader regional scope, the array will be populated with the names of the countries belonging to that region.
    :type supported_countries: List[str]
    """

    name: str = Field(description="Name of the destination")
    destination: str = Field(description="ISO3 representation of the destination")
    destination_iso2: str = Field(
        alias="destinationISO2",
        serialization_alias="destinationISO2",
        description="ISO2 representation of the destination",
    )
    supported_countries: List[str] = Field(
        alias="supportedCountries",
        serialization_alias="supportedCountries",
        description="This array indicates the geographical area covered by a specific destination. If the destination represents a single country, the array will include that country. However, if the destination represents a broader regional scope, the array will be populated with the names of the countries belonging to that region.",
    )


class ListDestinationsOkResponse(BaseModel):
    """ListDestinationsOkResponse

    :param destinations: destinations
    :type destinations: List[Destinations]
    """

    destinations: List[Destinations]
