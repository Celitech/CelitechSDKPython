from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .post_oauth2token_request_grant_type import PostOauth2TokenRequestGrantType


class PostOauth2TokenRequest(BaseModel):
    """PostOauth2TokenRequest

    :param grant_type: grant_type
    :type grant_type: PostOauth2TokenRequestGrantType
    :param client_id: client_id
    :type client_id: str
    :param client_secret: client_secret
    :type client_secret: str
    :param scope: scope
    :type scope: str
    """

    grant_type: PostOauth2TokenRequestGrantType = Field(default="client_credentials")
    client_id: str
    client_secret: str
    scope: str
