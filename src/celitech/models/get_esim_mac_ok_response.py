from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {"smdp_address": "smdpAddress", "manual_activation_code": "manualActivationCode"}
)
class GetEsimMacOkResponseEsim(BaseModel):
    """GetEsimMacOkResponseEsim

    :param iccid: ID of the eSIM
    :type iccid: str
    :param smdp_address: SM-DP+ Address
    :type smdp_address: str
    :param manual_activation_code: The manual activation code
    :type manual_activation_code: str
    """

    def __init__(
        self, iccid: str, smdp_address: str, manual_activation_code: str, **kwargs
    ):
        """GetEsimMacOkResponseEsim

        :param iccid: ID of the eSIM
        :type iccid: str
        :param smdp_address: SM-DP+ Address
        :type smdp_address: str
        :param manual_activation_code: The manual activation code
        :type manual_activation_code: str
        """
        self.iccid = self._define_str("iccid", iccid, min_length=18, max_length=22)
        self.smdp_address = smdp_address
        self.manual_activation_code = manual_activation_code
        self._kwargs = kwargs


@JsonMap({})
class GetEsimMacOkResponse(BaseModel):
    """GetEsimMacOkResponse

    :param esim: esim
    :type esim: GetEsimMacOkResponseEsim
    """

    def __init__(self, esim: GetEsimMacOkResponseEsim, **kwargs):
        """GetEsimMacOkResponse

        :param esim: esim
        :type esim: GetEsimMacOkResponseEsim
        """
        self.esim = self._define_object(esim, GetEsimMacOkResponseEsim)
        self._kwargs = kwargs
