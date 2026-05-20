from __future__ import annotations
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .grant_type import GrantType


class OAuthTokenRequest(BaseModel):
    """OAuthTokenRequest

    :param grant_type: grant_type
    :type grant_type: GrantType
    :param client_id: client_id
    :type client_id: str
    :param client_secret: client_secret
    :type client_secret: str
    :param scope: scope
    :type scope: str
    """

    grant_type: GrantType
    client_id: str
    client_secret: str
    scope: str
