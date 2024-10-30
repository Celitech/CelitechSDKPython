# PurchasesService

A list of all methods in the `PurchasesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                                                                                            |
| :---------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_purchases](#list_purchases)                     | This endpoint can be used to list all the successful purchases made between a given interval.                                                                                                                                                                                                                          |
| [create_purchase](#create_purchase)                   | This endpoint is used to purchase a new eSIM by providing the package details.                                                                                                                                                                                                                                         |
| [top_up_esim](#top_up_esim)                           | This endpoint is used to top-up an eSIM with the previously associated destination by providing an existing ICCID and the package details. The top-up is not feasible for eSIMs in "DELETED" or "ERROR" state.                                                                                                         |
| [edit_purchase](#edit_purchase)                       | This endpoint allows you to modify the dates of an existing package with a future activation start time. Editing can only be performed for packages that have not been activated, and it cannot change the package size. The modification must not change the package duration category to ensure pricing consistency. |
| [get_purchase_consumption](#get_purchase_consumption) | This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.                                                                                                                                       |

## list_purchases

This endpoint can be used to list all the successful purchases made between a given interval.

- HTTP Method: `GET`
- Endpoint: `/purchases`

**Parameters**

| Name         | Type  | Required | Description                                                                                                                                                                                                         |
| :----------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| iccid        | str   | ❌       | ID of the eSIM                                                                                                                                                                                                      |
| after_date   | str   | ❌       | Start date of the interval for filtering purchases in the format 'yyyy-MM-dd'                                                                                                                                       |
| before_date  | str   | ❌       | End date of the interval for filtering purchases in the format 'yyyy-MM-dd'                                                                                                                                         |
| reference_id | str   | ❌       | The referenceId that was provided by the partner during the purchase or topup flow.                                                                                                                                 |
| after_cursor | str   | ❌       | To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data. |
| limit        | float | ❌       | Maximum number of purchases to be returned in the response. The value must be greater than 0 and less than or equal to 100. If not provided, the default value is 20                                                |
| after        | float | ❌       | Epoch value representing the start of the time interval for filtering purchases                                                                                                                                     |
| before       | float | ❌       | Epoch value representing the end of the time interval for filtering purchases                                                                                                                                       |

**Return Type**

`ListPurchasesOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

result = sdk.purchases.list_purchases()

print(result)
```

## create_purchase

This endpoint is used to purchase a new eSIM by providing the package details.

- HTTP Method: `POST`
- Endpoint: `/purchases`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreatePurchaseRequest](../models/CreatePurchaseRequest.md) | ✅       | The request body. |

**Return Type**

`CreatePurchaseOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import CreatePurchaseRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

request_body = CreatePurchaseRequest(
    destination="FRA",
    data_limit_in_gb=1,
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.create_purchase(request_body=request_body)

print(result)
```

## top_up_esim

This endpoint is used to top-up an eSIM with the previously associated destination by providing an existing ICCID and the package details. The top-up is not feasible for eSIMs in "DELETED" or "ERROR" state.

- HTTP Method: `POST`
- Endpoint: `/purchases/topup`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [TopUpEsimRequest](../models/TopUpEsimRequest.md) | ✅       | The request body. |

**Return Type**

`TopUpEsimOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import TopUpEsimRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

request_body = TopUpEsimRequest(
    iccid="1111222233334444555000",
    data_limit_in_gb=1,
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.top_up_esim(request_body=request_body)

print(result)
```

## edit_purchase

This endpoint allows you to modify the dates of an existing package with a future activation start time. Editing can only be performed for packages that have not been activated, and it cannot change the package size. The modification must not change the package duration category to ensure pricing consistency.

- HTTP Method: `POST`
- Endpoint: `/purchases/edit`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditPurchaseRequest](../models/EditPurchaseRequest.md) | ✅       | The request body. |

**Return Type**

`EditPurchaseOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import EditPurchaseRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

request_body = EditPurchaseRequest(
    purchase_id="ae471106-c8b4-42cf-b83a-b061291f2922",
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.edit_purchase(request_body=request_body)

print(result)
```

## get_purchase_consumption

This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

- HTTP Method: `GET`
- Endpoint: `/purchases/{purchaseId}/consumption`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| purchase_id | str  | ✅       | ID of the purchase |

**Return Type**

`GetPurchaseConsumptionOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

result = sdk.purchases.get_purchase_consumption(purchase_id="4973fa15-6979-4daa-9cf3-672620df819c")

print(result)
```
