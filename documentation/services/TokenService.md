# TokenService

A list of all methods in the `TokenService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                   |
| :-------------------------------- | :-------------------------------------------- |
| [generate_token](#generate_token) | Generate a new token to be used in the iFrame |

## generate_token

Generate a new token to be used in the iFrame

- HTTP Method: `POST`
- Endpoint: `/iframe/token`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| accept | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.token.generate_token(accept="application/json")

print(result)
```
