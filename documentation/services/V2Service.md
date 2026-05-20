# V2Service

A list of all methods in the `V2Service` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                                                                    |
| :---------------------------------------- | :----------------------------------------------------------------------------- |
| [create_purchase_v2](#create_purchase_v2) | This endpoint is used to purchase a new eSIM by providing the package details. |

## create_purchase_v2

This endpoint is used to purchase a new eSIM by providing the package details.

- HTTP Method: `POST`
- Endpoint: `/purchases/v2`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreatePurchaseV2Request](../models/CreatePurchaseV2Request.md) | ✅       | The request body. |
| accept       | str                                                             | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import CreatePurchaseV2Request

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = CreatePurchaseV2Request(

)

result = sdk.v2.create_purchase_v2(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
