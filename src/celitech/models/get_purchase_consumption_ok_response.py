from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "data_usage_remaining_in_bytes": "dataUsageRemainingInBytes",
        "data_usage_remaining_in_gb": "dataUsageRemainingInGB",
    }
)
class GetPurchaseConsumptionOkResponse(BaseModel):
    """GetPurchaseConsumptionOkResponse

    :param data_usage_remaining_in_bytes: Remaining balance of the package in bytes
    :type data_usage_remaining_in_bytes: float
    :param data_usage_remaining_in_gb: Remaining balance of the package in GB
    :type data_usage_remaining_in_gb: float
    :param status: Status of the connectivity, possible values are 'ACTIVE' or 'NOT_ACTIVE'
    :type status: str
    """

    def __init__(
        self,
        data_usage_remaining_in_bytes: float,
        data_usage_remaining_in_gb: float,
        status: str,
        **kwargs
    ):
        """GetPurchaseConsumptionOkResponse

        :param data_usage_remaining_in_bytes: Remaining balance of the package in bytes
        :type data_usage_remaining_in_bytes: float
        :param data_usage_remaining_in_gb: Remaining balance of the package in GB
        :type data_usage_remaining_in_gb: float
        :param status: Status of the connectivity, possible values are 'ACTIVE' or 'NOT_ACTIVE'
        :type status: str
        """
        self.data_usage_remaining_in_bytes = self._define_number(
            "data_usage_remaining_in_bytes", data_usage_remaining_in_bytes
        )
        self.data_usage_remaining_in_gb = self._define_number(
            "data_usage_remaining_in_gb", data_usage_remaining_in_gb
        )
        self.status = self._define_str("status", status)
        self._kwargs = kwargs
