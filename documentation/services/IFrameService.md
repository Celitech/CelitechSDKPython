# IFrameService

A list of all methods in the `IFrameService` service. Click on the method name to view detailed information about that method.

| Methods         | Description                                   |
| :-------------- | :-------------------------------------------- |
| [token](#token) | Generate a new token to be used in the iFrame |

## token

Generate a new token to be used in the iFrame

- HTTP Method: `POST`
- Endpoint: `/iframe/token`

**Return Type**

[`TokenResponse`](../models/TokenResponse.md)

**Example Usage Code Snippet**

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
result = client.i_frame.token()

print(result)
```
