```python
from celitech import Celitech
from celitech.models import GetAccessTokenRequest

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = GetAccessTokenRequest(

)

result = sdk.o_auth.get_access_token(request_body=request_body)

print(result)

```
