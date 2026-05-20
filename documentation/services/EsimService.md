# EsimService

A list of all methods in the `EsimService` service. Click on the method name to view detailed information about that method.

| Methods                 | Description |
| :---------------------- | :---------- |
| [get_e_sim](#get_e_sim) | Get eSIM    |

## get_e_sim

Get eSIM

- HTTP Method: `GET`
- Endpoint: `/esim`

**Parameters**

| Name   | Type | Required | Description    |
| :----- | :--- | :------- | :------------- |
| accept | str  | ✅       |                |
| iccid  | str  | ❌       | ID of the eSIM |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.esim.get_e_sim(accept="application/json")

print(result)
```
