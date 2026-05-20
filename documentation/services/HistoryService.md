# HistoryService

A list of all methods in the `HistoryService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description      |
| :-------------------------------------- | :--------------- |
| [get_e_sim_history](#get_e_sim_history) | Get eSIM History |

## get_e_sim_history

Get eSIM History

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/history`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| iccid  | str  | ✅       |             |
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

result = sdk.history.get_e_sim_history(
    iccid="iccid",
    accept="application/json"
)

print(result)
```
