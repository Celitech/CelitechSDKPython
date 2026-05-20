# DeviceService

A list of all methods in the `DeviceService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description     |
| :------------------------------------ | :-------------- |
| [get_e_sim_device](#get_e_sim_device) | Get eSIM Device |

## get_e_sim_device

Get eSIM Device

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/device`

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

result = sdk.device.get_e_sim_device(
    iccid="iccid",
    accept="application/json"
)

print(result)
```
