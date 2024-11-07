# OAuthService

A list of all methods in the `OAuthService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                       |
| :------------------------------------ | :-------------------------------- |
| [get_access_token](#get_access_token) | This endpoint was added by liblab |

## get_access_token

This endpoint was added by liblab

- HTTP Method: `POST`
- Endpoint: `/oauth2/token`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [GetAccessTokenRequest](../models/GetAccessTokenRequest.md) | ✅       | The request body. |

**Return Type**

`GetAccessTokenOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import GetAccessTokenRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = GetAccessTokenRequest(

)

result = sdk.o_auth.get_access_token(request_body=request_body)

print(result)
```
