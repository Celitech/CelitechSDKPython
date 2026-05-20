from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class Package(BaseModel):
    """Package

    :param id_: ID of the package
    :type id_: str
    :param data_limit_in_bytes: Size of the package in Bytes
    :type data_limit_in_bytes: float
    :param data_limit_in_gb: Size of the package in GB
    :type data_limit_in_gb: float
    :param destination: ISO3 representation of the package's destination.
    :type destination: str
    :param destination_iso2: ISO2 representation of the package's destination.
    :type destination_iso2: str
    :param destination_name: Name of the package's destination
    :type destination_name: str
    :param price_in_cents: Price of the package in cents
    :type price_in_cents: float
    """

    id_: str = Field(
        alias="id", serialization_alias="id", description="ID of the package"
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
    destination: str = Field(
        description="ISO3 representation of the package's destination."
    )
    destination_iso2: str = Field(
        alias="destinationISO2",
        serialization_alias="destinationISO2",
        description="ISO2 representation of the package's destination.",
    )
    destination_name: str = Field(
        alias="destinationName",
        serialization_alias="destinationName",
        description="Name of the package's destination",
    )
    price_in_cents: float = Field(
        alias="priceInCents",
        serialization_alias="priceInCents",
        description="Price of the package in cents",
    )


class PurchasesEsim(BaseModel):
    """PurchasesEsim

    :param iccid: ID of the eSIM
    :type iccid: str
    """

    iccid: str = Field(description="ID of the eSIM", min_length=18, max_length=22)


class Purchases(BaseModel):
    """Purchases

    :param id_: ID of the purchase
    :type id_: str
    :param start_date: Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type start_date: str
    :param end_date: End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type end_date: str
    :param duration: Duration of the package in days. Possible values are 1, 2, 7, 14, 30, or 90., defaults to None
    :type duration: float, optional
    :param created_date: Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type created_date: str
    :param start_time: Epoch value representing the start time of the package's validity, defaults to None
    :type start_time: float, optional
    :param end_time: Epoch value representing the end time of the package's validity, defaults to None
    :type end_time: float, optional
    :param created_at: Epoch value representing the date of creation of the purchase, defaults to None
    :type created_at: float, optional
    :param package: package
    :type package: Package
    :param esim: esim
    :type esim: PurchasesEsim
    :param source: The `source` indicates whether the purchase was made from the API, dashboard, landing-page, promo-page or iframe. For purchases made before September 8, 2023, the value will be displayed as 'Not available'.
    :type source: str
    :param purchase_type: The `purchaseType` indicates whether this is the initial purchase that creates the eSIM (First Purchase) or a subsequent top-up on an existing eSIM (Top-up Purchase).
    :type purchase_type: str
    :param reference_id: The `referenceId` that was provided by the partner during the purchase or top-up flow. This identifier can be used for analytics and debugging purposes., defaults to None
    :type reference_id: str, optional
    """

    id_: str = Field(
        alias="id", serialization_alias="id", description="ID of the purchase"
    )
    start_date: Optional[str] = Field(
        alias="startDate",
        serialization_alias="startDate",
        description="Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    end_date: Optional[str] = Field(
        alias="endDate",
        serialization_alias="endDate",
        description="End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    duration: Optional[float] = Field(
        default=None,
        description="Duration of the package in days. Possible values are 1, 2, 7, 14, 30, or 90.",
    )
    created_date: str = Field(
        alias="createdDate",
        serialization_alias="createdDate",
        description="Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    start_time: Optional[float] = Field(
        alias="startTime",
        serialization_alias="startTime",
        default=None,
        description="Epoch value representing the start time of the package's validity",
    )
    end_time: Optional[float] = Field(
        alias="endTime",
        serialization_alias="endTime",
        default=None,
        description="Epoch value representing the end time of the package's validity",
    )
    created_at: Optional[float] = Field(
        alias="createdAt",
        serialization_alias="createdAt",
        default=None,
        description="Epoch value representing the date of creation of the purchase",
    )
    package: Package
    esim: PurchasesEsim
    source: str = Field(
        description="The `source` indicates whether the purchase was made from the API, dashboard, landing-page, promo-page or iframe. For purchases made before September 8, 2023, the value will be displayed as 'Not available'."
    )
    purchase_type: str = Field(
        alias="purchaseType",
        serialization_alias="purchaseType",
        description="The `purchaseType` indicates whether this is the initial purchase that creates the eSIM (First Purchase) or a subsequent top-up on an existing eSIM (Top-up Purchase).",
    )
    reference_id: Optional[str] = Field(
        alias="referenceId",
        serialization_alias="referenceId",
        default=None,
        description="The `referenceId` that was provided by the partner during the purchase or top-up flow. This identifier can be used for analytics and debugging purposes.",
    )


class ListPurchasesOkResponse(BaseModel):
    """ListPurchasesOkResponse

    :param purchases: purchases
    :type purchases: List[Purchases]
    :param after_cursor: The cursor value representing the end of the current page of results. Use this cursor value as the "afterCursor" parameter in your next request to retrieve the subsequent page of results. It ensures that you continue fetching data from where you left off, facilitating smooth pagination.
    :type after_cursor: str
    """

    purchases: List[Purchases]
    after_cursor: Optional[str] = Field(
        alias="afterCursor",
        serialization_alias="afterCursor",
        description='The cursor value representing the end of the current page of results. Use this cursor value as the "afterCursor" parameter in your next request to retrieve the subsequent page of results. It ensures that you continue fetching data from where you left off, facilitating smooth pagination.',
    )
