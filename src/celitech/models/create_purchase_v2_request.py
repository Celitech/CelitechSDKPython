from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "data_limit_in_gb": "dataLimitInGB",
        "start_date": "startDate",
        "end_date": "endDate",
        "reference_id": "referenceId",
        "network_brand": "networkBrand",
    }
)
class CreatePurchaseV2Request(BaseModel):
    """CreatePurchaseV2Request

    :param destination: ISO representation of the package's destination
    :type destination: str
    :param data_limit_in_gb: Size of the package in GB. - **Limited Packages (1, 2, 3, 5, 8, 20GB):** supports `duration` or `startDate` / `endDate`. - **Unlimited Packages (available for Region-3):** supports `duration` only. Use **-1** for unlimited.
    :type data_limit_in_gb: float
    :param start_date: Start date of the package validity in the format yyyy-MM-dd. This date can be set to the current day or any day within the next 12 months.  Exactly one of the following must be provided: - Both `startDate` and `endDate` together - Or `duration` alone These options are mutually exclusive — do not include `duration` with `startDate` or `endDate`. , defaults to None
    :type start_date: str, optional
    :param end_date: End date of the package validity in the format yyyy-MM-dd. End date can be maximum 90 days after Start date.  Exactly one of the following must be provided: - Both `startDate` and `endDate` together - Or `duration` alone These options are mutually exclusive — do not include `duration` with `startDate` or `endDate`. , defaults to None
    :type end_date: str, optional
    :param duration: It designates the number of days the eSIM is valid for within 90-day validity from issuance date.  - **For limited packages** (1, 2, 3, 5, 8, 20GB): The available options are 1, 2, 7, 14, 30 days (following the pricing of 0-30 days) and 90 days (following the pricing of 0-90 days)  - **For unlimited package** (available for Region-3): The available options are for 1, 2, 7, 14, 30 days (following a custom pricing).  Exactly one of the following must be provided:  - Both `startDate` and `endDate` together  - Or `duration` alone  These options are mutually exclusive — do not include `duration` with `startDate` or `endDate`. , defaults to None
    :type duration: float, optional
    :param quantity: Number of eSIMs to purchase.
    :type quantity: float
    :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
    :type email: str, optional
    :param reference_id: An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes., defaults to None
    :type reference_id: str, optional
    :param network_brand: Customize the network brand of the issued eSIM. This parameter is accessible to platforms with Diamond tier and requires an alphanumeric string of up to 15 characters., defaults to None
    :type network_brand: str, optional
    """

    def __init__(
        self,
        destination: str,
        data_limit_in_gb: float,
        quantity: float,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        **kwargs
    ):
        """CreatePurchaseV2Request

        :param destination: ISO representation of the package's destination
        :type destination: str
        :param data_limit_in_gb: Size of the package in GB. - **Limited Packages (1, 2, 3, 5, 8, 20GB):** supports `duration` or `startDate` / `endDate`. - **Unlimited Packages (available for Region-3):** supports `duration` only. Use **-1** for unlimited.
        :type data_limit_in_gb: float
        :param start_date: Start date of the package validity in the format yyyy-MM-dd. This date can be set to the current day or any day within the next 12 months.  Exactly one of the following must be provided: - Both `startDate` and `endDate` together - Or `duration` alone These options are mutually exclusive — do not include `duration` with `startDate` or `endDate`. , defaults to None
        :type start_date: str, optional
        :param end_date: End date of the package validity in the format yyyy-MM-dd. End date can be maximum 90 days after Start date.  Exactly one of the following must be provided: - Both `startDate` and `endDate` together - Or `duration` alone These options are mutually exclusive — do not include `duration` with `startDate` or `endDate`. , defaults to None
        :type end_date: str, optional
        :param duration: It designates the number of days the eSIM is valid for within 90-day validity from issuance date.  - **For limited packages** (1, 2, 3, 5, 8, 20GB): The available options are 1, 2, 7, 14, 30 days (following the pricing of 0-30 days) and 90 days (following the pricing of 0-90 days)  - **For unlimited package** (available for Region-3): The available options are for 1, 2, 7, 14, 30 days (following a custom pricing).  Exactly one of the following must be provided:  - Both `startDate` and `endDate` together  - Or `duration` alone  These options are mutually exclusive — do not include `duration` with `startDate` or `endDate`. , defaults to None
        :type duration: float, optional
        :param quantity: Number of eSIMs to purchase.
        :type quantity: float
        :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
        :type email: str, optional
        :param reference_id: An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes., defaults to None
        :type reference_id: str, optional
        :param network_brand: Customize the network brand of the issued eSIM. This parameter is accessible to platforms with Diamond tier and requires an alphanumeric string of up to 15 characters., defaults to None
        :type network_brand: str, optional
        """
        self.destination = destination
        self.data_limit_in_gb = data_limit_in_gb
        self.start_date = self._define_str("start_date", start_date, nullable=True)
        self.end_date = self._define_str("end_date", end_date, nullable=True)
        self.duration = self._define_number("duration", duration, nullable=True)
        self.quantity = self._define_number("quantity", quantity, ge=1, le=5)
        self.email = self._define_str("email", email, nullable=True)
        self.reference_id = self._define_str(
            "reference_id", reference_id, nullable=True
        )
        self.network_brand = self._define_str(
            "network_brand", network_brand, nullable=True
        )
        self._kwargs = kwargs
