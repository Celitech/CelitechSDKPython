# TopupService

A list of all methods in the `TopupService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                                                                                                                                                                                                                                           |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [top_up_e_sim](#top_up_e_sim) | This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag. |

## top_up_e_sim

This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

- HTTP Method: `POST`
- Endpoint: `/purchases/topup`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [TopUpESimRequest](../models/TopUpESimRequest.md) | ✅       | The request body. |
| accept       | str                                               | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import TopUpESimRequest

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = TopUpESimRequest(

)

result = sdk.topup.top_up_e_sim(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
