from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class GetAccessTokenOkResponse(BaseModel):
    """GetAccessTokenOkResponse

    :param access_token: access_token, defaults to None
    :type access_token: str, optional
    :param token_type: token_type, defaults to None
    :type token_type: str, optional
    :param expires_in: expires_in, defaults to None
    :type expires_in: int, optional
    """

    access_token: Optional[str] = Field(default=None)
    token_type: Optional[str] = Field(default=None)
    expires_in: Optional[int] = Field(default=None)
