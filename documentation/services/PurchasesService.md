# PurchasesService

A list of all methods in the `PurchasesService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                                                                                   |
| :---------------------------------- | :-------------------------------------------------------------------------------------------- |
| [create_purchase](#create_purchase) | This endpoint is used to purchase a new eSIM by providing the package details.                |
| [list_purchases](#list_purchases)   | This endpoint can be used to list all the successful purchases made between a given interval. |

## create_purchase

This endpoint is used to purchase a new eSIM by providing the package details.

- HTTP Method: `POST`
- Endpoint: `/purchases`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreatePurchaseRequest](../models/CreatePurchaseRequest.md) | ✅       | The request body. |
| accept       | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import CreatePurchaseRequest

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = CreatePurchaseRequest(

)

result = sdk.purchases.create_purchase(
    request_body=request_body,
    accept="application/json"
)

print(result)
```

## list_purchases

This endpoint can be used to list all the successful purchases made between a given interval.

- HTTP Method: `GET`
- Endpoint: `/purchases`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                                         |
| :----------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| accept       | str  | ✅       |                                                                                                                                                                                                                     |
| purchase_id  | str  | ❌       | ID of the purchase                                                                                                                                                                                                  |
| iccid        | str  | ❌       | ID of the eSIM                                                                                                                                                                                                      |
| after_date   | str  | ❌       | Start date of the interval for filtering purchases in the format 'yyyy-MM-dd'                                                                                                                                       |
| before_date  | str  | ❌       | End date of the interval for filtering purchases in the format 'yyyy-MM-dd'                                                                                                                                         |
| email        | str  | ❌       | Email associated to the purchase.                                                                                                                                                                                   |
| reference_id | str  | ❌       | The referenceId that was provided by the partner during the purchase or topup flow.                                                                                                                                 |
| after_cursor | str  | ❌       | To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data. |
| limit        | str  | ❌       | Maximum number of purchases to be returned in the response. The value must be greater than 0 and less than or equal to 100. If not provided, the default value is 20                                                |
| after        | str  | ❌       | Epoch value representing the start of the time interval for filtering purchases                                                                                                                                     |
| before       | str  | ❌       | Epoch value representing the end of the time interval for filtering purchases                                                                                                                                       |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.purchases.list_purchases(accept="application/json")

print(result)
```
