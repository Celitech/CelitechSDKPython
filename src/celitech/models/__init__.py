from .list_destinations_ok_response import ListDestinationsOkResponse, Destinations
from .list_packages_ok_response import ListPackagesOkResponse, Packages
from .create_purchase_v2_request import (
    CreatePurchaseV2Request,
    CreatePurchaseV2RequestLanguage,
)
from .create_purchase_v2_ok_response import (
    CreatePurchaseV2OkResponse,
    CreatePurchaseV2OkResponsePurchase,
    CreatePurchaseV2OkResponseProfile,
)
from .list_purchases_ok_response import ListPurchasesOkResponse, Purchases
from .create_purchase_request import (
    CreatePurchaseRequest,
    CreatePurchaseRequestLanguage,
)
from .create_purchase_ok_response import (
    CreatePurchaseOkResponse,
    CreatePurchaseOkResponsePurchase,
    CreatePurchaseOkResponseProfile,
)
from .top_up_esim_request import TopUpEsimRequest
from .top_up_esim_ok_response import (
    TopUpEsimOkResponse,
    TopUpEsimOkResponsePurchase,
    TopUpEsimOkResponseProfile,
)
from .edit_purchase_request import EditPurchaseRequest
from .edit_purchase_ok_response import EditPurchaseOkResponse
from .get_purchase_consumption_ok_response import GetPurchaseConsumptionOkResponse
from .get_esim_ok_response import GetEsimOkResponse, GetEsimOkResponseEsim
from .get_esim_device_ok_response import GetEsimDeviceOkResponse, Device
from .get_esim_history_ok_response import (
    GetEsimHistoryOkResponse,
    GetEsimHistoryOkResponseEsim,
)
from .token_ok_response import TokenOkResponse
from .o_auth_token_request import OAuthTokenRequest
from .o_auth_token_response import OAuthTokenResponse
from .grant_type import GrantType
from .bad_request import BadRequest
from .unauthorized import Unauthorized

# Rebuild models to resolve circular forward references
# This ensures Pydantic can properly validate models that reference each other
ListDestinationsOkResponse.model_rebuild()
Destinations.model_rebuild()
ListPackagesOkResponse.model_rebuild()
Packages.model_rebuild()
CreatePurchaseV2Request.model_rebuild()
CreatePurchaseV2OkResponse.model_rebuild()
CreatePurchaseV2OkResponsePurchase.model_rebuild()
CreatePurchaseV2OkResponseProfile.model_rebuild()
ListPurchasesOkResponse.model_rebuild()
Purchases.model_rebuild()
CreatePurchaseRequest.model_rebuild()
CreatePurchaseOkResponse.model_rebuild()
CreatePurchaseOkResponsePurchase.model_rebuild()
CreatePurchaseOkResponseProfile.model_rebuild()
TopUpEsimRequest.model_rebuild()
TopUpEsimOkResponse.model_rebuild()
TopUpEsimOkResponsePurchase.model_rebuild()
TopUpEsimOkResponseProfile.model_rebuild()
EditPurchaseRequest.model_rebuild()
EditPurchaseOkResponse.model_rebuild()
GetPurchaseConsumptionOkResponse.model_rebuild()
GetEsimOkResponse.model_rebuild()
GetEsimOkResponseEsim.model_rebuild()
GetEsimDeviceOkResponse.model_rebuild()
Device.model_rebuild()
GetEsimHistoryOkResponse.model_rebuild()
GetEsimHistoryOkResponseEsim.model_rebuild()
TokenOkResponse.model_rebuild()
OAuthTokenRequest.model_rebuild()
OAuthTokenResponse.model_rebuild()
