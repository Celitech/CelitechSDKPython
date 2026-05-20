from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class OAuthTokenResponse(BaseModel):
    """OAuthTokenResponse

    :param access_token: access_token, defaults to None
    :type access_token: str, optional
    :param expires_in: expires_in, defaults to None
    :type expires_in: int, optional
    """

    access_token: Optional[str] = Field(default=None)
    expires_in: Optional[int] = Field(default=None)
