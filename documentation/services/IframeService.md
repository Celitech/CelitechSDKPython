# IframeService

A list of all methods in the `IframeService` service. Click on the method name to view detailed information about that method.

| Methods         | Description                                   |
| :-------------- | :-------------------------------------------- |
| [token](#token) | Generate a new token to be used in the iFrame |

## token

Generate a new token to be used in the iFrame

- HTTP Method: `POST`
- Endpoint: `/iframe/token`

**Return Type**

`TokenOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.iframe.token()

print(result)
```
