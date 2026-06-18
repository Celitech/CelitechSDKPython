"""Lazy model exports.

Names are resolved on first attribute access via PEP 562 ``__getattr__``,
then cached in module globals. Avoids the multi-second eager-import cost
on SDKs with thousands of generated models.
"""

import importlib

_MODEL_TO_MODULE = {
    "ListDestinationsOkResponse": "list_destinations_ok_response",
    "Destinations": "list_destinations_ok_response",
    "ListPackagesOkResponse": "list_packages_ok_response",
    "Packages": "list_packages_ok_response",
    "CreatePurchaseV2Request": "create_purchase_v2_request",
    "CreatePurchaseV2RequestLanguage": "create_purchase_v2_request",
    "CreatePurchaseV2OkResponse": "create_purchase_v2_ok_response",
    "CreatePurchaseV2OkResponsePurchase": "create_purchase_v2_ok_response",
    "CreatePurchaseV2OkResponseProfile": "create_purchase_v2_ok_response",
    "ListPurchasesOkResponse": "list_purchases_ok_response",
    "Purchases": "list_purchases_ok_response",
    "CreatePurchaseRequest": "create_purchase_request",
    "CreatePurchaseRequestLanguage": "create_purchase_request",
    "CreatePurchaseOkResponse": "create_purchase_ok_response",
    "CreatePurchaseOkResponsePurchase": "create_purchase_ok_response",
    "CreatePurchaseOkResponseProfile": "create_purchase_ok_response",
    "TopUpEsimRequest": "top_up_esim_request",
    "TopUpEsimOkResponse": "top_up_esim_ok_response",
    "TopUpEsimOkResponsePurchase": "top_up_esim_ok_response",
    "TopUpEsimOkResponseProfile": "top_up_esim_ok_response",
    "EditPurchaseRequest": "edit_purchase_request",
    "EditPurchaseOkResponse": "edit_purchase_ok_response",
    "GetPurchaseConsumptionOkResponse": "get_purchase_consumption_ok_response",
    "GetEsimOkResponse": "get_esim_ok_response",
    "GetEsimOkResponseEsim": "get_esim_ok_response",
    "GetEsimDeviceOkResponse": "get_esim_device_ok_response",
    "Device": "get_esim_device_ok_response",
    "GetEsimHistoryOkResponse": "get_esim_history_ok_response",
    "GetEsimHistoryOkResponseEsim": "get_esim_history_ok_response",
    "TokenOkResponse": "token_ok_response",
    "OAuthTokenRequest": "o_auth_token_request",
    "OAuthTokenResponse": "o_auth_token_response",
    "GrantType": "grant_type",
    "BadRequest": "bad_request",
    "Unauthorized": "unauthorized",
}

_REBUILD_NAMES = frozenset(
    {
        "ListDestinationsOkResponse",
        "Destinations",
        "ListPackagesOkResponse",
        "Packages",
        "CreatePurchaseV2Request",
        "CreatePurchaseV2OkResponse",
        "CreatePurchaseV2OkResponsePurchase",
        "CreatePurchaseV2OkResponseProfile",
        "ListPurchasesOkResponse",
        "Purchases",
        "CreatePurchaseRequest",
        "CreatePurchaseOkResponse",
        "CreatePurchaseOkResponsePurchase",
        "CreatePurchaseOkResponseProfile",
        "TopUpEsimRequest",
        "TopUpEsimOkResponse",
        "TopUpEsimOkResponsePurchase",
        "TopUpEsimOkResponseProfile",
        "EditPurchaseRequest",
        "EditPurchaseOkResponse",
        "GetPurchaseConsumptionOkResponse",
        "GetEsimOkResponse",
        "GetEsimOkResponseEsim",
        "GetEsimDeviceOkResponse",
        "Device",
        "GetEsimHistoryOkResponse",
        "GetEsimHistoryOkResponseEsim",
        "TokenOkResponse",
        "OAuthTokenRequest",
        "OAuthTokenResponse",
    }
)

__all__ = list(_MODEL_TO_MODULE.keys())

_rebuilt = False


def _load(name):
    module = _MODEL_TO_MODULE.get(name)
    if module is None:
        return None
    obj = getattr(importlib.import_module("." + module, __name__), name)
    globals()[name] = obj
    return obj


def _ensure_rebuilt():
    """Resolve forward refs across every BaseModel in one batched pass.

    Individual model files import their cross-references inside a
    ``TYPE_CHECKING`` block, so at runtime each file's globals contain
    only itself. ``model_rebuild()`` walks the call stack to find
    forward-ref names — calling it from this module once every
    BaseModel has been loaded into our globals is what lets pydantic
    resolve circular refs (the same shape the prior eager-import form
    relied on). Enums, Union types, and error models stay lazy.
    """
    global _rebuilt
    if _rebuilt:
        return
    _rebuilt = True
    for name in _REBUILD_NAMES:
        if name not in globals():
            try:
                _load(name)
            except Exception:
                pass
    ns = globals()
    for name in _REBUILD_NAMES:
        cls = ns.get(name)
        if cls is None:
            continue
        try:
            # _types_namespace is mandatory: pydantic resolves forward refs
            # against caller-frame locals by default, but we're calling from
            # inside a helper — the names live in this module's globals.
            cls.model_rebuild(_types_namespace=ns)
        except Exception:
            pass


def __getattr__(name):
    if name not in _MODEL_TO_MODULE:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    obj = _load(name)
    if name in _REBUILD_NAMES:
        _ensure_rebuilt()
    return obj


def __dir__():
    return sorted(set(globals()).union(_MODEL_TO_MODULE))
