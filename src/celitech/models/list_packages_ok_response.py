from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class Packages(BaseModel):
    """Packages

    :param id_: ID of the package
    :type id_: str
    :param destination: ISO3 representation of the package's destination.
    :type destination: str
    :param destination_iso2: ISO2 representation of the package's destination.
    :type destination_iso2: str
    :param data_limit_in_bytes: Size of the package in Bytes
    :type data_limit_in_bytes: float
    :param data_limit_in_gb: Size of the package in GB
    :type data_limit_in_gb: float
    :param min_days: Min number of days for the package
    :type min_days: float
    :param max_days: Max number of days for the package
    :type max_days: float
    :param price_in_cents: Price of the package in cents
    :type price_in_cents: float
    """

    id_: str = Field(
        alias="id", serialization_alias="id", description="ID of the package"
    )
    destination: str = Field(
        description="ISO3 representation of the package's destination."
    )
    destination_iso2: str = Field(
        alias="destinationISO2",
        serialization_alias="destinationISO2",
        description="ISO2 representation of the package's destination.",
    )
    data_limit_in_bytes: float = Field(
        alias="dataLimitInBytes",
        serialization_alias="dataLimitInBytes",
        description="Size of the package in Bytes",
    )
    data_limit_in_gb: float = Field(
        alias="dataLimitInGB",
        serialization_alias="dataLimitInGB",
        description="Size of the package in GB",
    )
    min_days: float = Field(
        alias="minDays",
        serialization_alias="minDays",
        description="Min number of days for the package",
    )
    max_days: float = Field(
        alias="maxDays",
        serialization_alias="maxDays",
        description="Max number of days for the package",
    )
    price_in_cents: float = Field(
        alias="priceInCents",
        serialization_alias="priceInCents",
        description="Price of the package in cents",
    )


class ListPackagesOkResponse(BaseModel):
    """ListPackagesOkResponse

    :param packages: packages
    :type packages: List[Packages]
    :param after_cursor: The cursor value representing the end of the current page of results. Use this cursor value as the "afterCursor" parameter in your next request to retrieve the subsequent page of results. It ensures that you continue fetching data from where you left off, facilitating smooth pagination
    :type after_cursor: str
    """

    packages: List[Packages]
    after_cursor: Optional[str] = Field(
        alias="afterCursor",
        serialization_alias="afterCursor",
        description='The cursor value representing the end of the current page of results. Use this cursor value as the "afterCursor" parameter in your next request to retrieve the subsequent page of results. It ensures that you continue fetching data from where you left off, facilitating smooth pagination',
    )
