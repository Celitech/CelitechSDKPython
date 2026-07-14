# CelitechService

A list of all methods in the `CelitechService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_destinations](#list_destinations)               | List Destinations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [list_packages](#list_packages)                       | List Packages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [create_purchase_v2](#create_purchase_v2)             | This endpoint is used to purchase a new eSIM by providing the package details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [top_up_e_sim](#top_up_e_sim)                         | This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.                                                                                                                                                                                                                                                                                                                                                                                                    |
| [edit_purchase](#edit_purchase)                       | This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits. |
| [get_purchase_consumption](#get_purchase_consumption) | This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [create_purchase](#create_purchase)                   | This endpoint is used to purchase a new eSIM by providing the package details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [list_purchases](#list_purchases)                     | This endpoint can be used to list all the successful purchases made between a given interval.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [get_e_sim_device](#get_e_sim_device)                 | Get eSIM Device                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_e_sim_history](#get_e_sim_history)               | Get eSIM History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [get_e_sim](#get_e_sim)                               | Get eSIM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [generate_token](#generate_token)                     | Generate a new token to be used in the iFrame                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## list_destinations

List Destinations

- HTTP Method: `GET`
- Endpoint: `/destinations`

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.list_destinations()

print(result)
```

## list_packages

List Packages

- HTTP Method: `GET`
- Endpoint: `/packages`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                                         |
| :----------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| destination  | str  | ❌       | ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.                                                                                              |
| start_date   | str  | ❌       | Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.                                                                      |
| end_date     | str  | ❌       | End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.                                                                                                    |
| after_cursor | str  | ❌       | To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data. |
| limit        | str  | ❌       | Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20                                                 |
| start_time   | str  | ❌       | Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months                                                              |
| end_time     | str  | ❌       | Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time                                                                                                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.list_packages()

print(result)
```

## create_purchase_v2

This endpoint is used to purchase a new eSIM by providing the package details.

- HTTP Method: `POST`
- Endpoint: `/purchases/v2`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreatePurchaseV2Request](../models/CreatePurchaseV2Request.md) | ✅       | The request body. |

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

result = sdk.celitech.create_purchase_v2(request_body=request_body)

print(result)
```

## top_up_e_sim

This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

- HTTP Method: `POST`
- Endpoint: `/purchases/topup`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [TopUpESimRequest](../models/TopUpESimRequest.md) | ✅       | The request body. |

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

result = sdk.celitech.top_up_e_sim(request_body=request_body)

print(result)
```

## edit_purchase

This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

- HTTP Method: `POST`
- Endpoint: `/purchases/edit`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditPurchaseRequest](../models/EditPurchaseRequest.md) | ✅       | The request body. |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech
from celitech.models import EditPurchaseRequest

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = EditPurchaseRequest(

)

result = sdk.celitech.edit_purchase(request_body=request_body)

print(result)
```

## get_purchase_consumption

This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

- HTTP Method: `GET`
- Endpoint: `/purchases/{purchaseId}/consumption`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| purchase_id | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.get_purchase_consumption(purchase_id="purchaseId")

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

result = sdk.celitech.create_purchase(request_body=request_body)

print(result)
```

## list_purchases

This endpoint can be used to list all the successful purchases made between a given interval.

- HTTP Method: `GET`
- Endpoint: `/purchases`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                                         |
| :----------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
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

result = sdk.celitech.list_purchases()

print(result)
```

## get_e_sim_device

Get eSIM Device

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/device`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| iccid | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.get_e_sim_device(iccid="iccid")

print(result)
```

## get_e_sim_history

Get eSIM History

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/history`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| iccid | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.get_e_sim_history(iccid="iccid")

print(result)
```

## get_e_sim

Get eSIM

- HTTP Method: `GET`
- Endpoint: `/esim`

**Parameters**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ❌       | ID of the eSIM |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.get_e_sim()

print(result)
```

## generate_token

Generate a new token to be used in the iFrame

- HTTP Method: `POST`
- Endpoint: `/iframe/token`

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.celitech.generate_token()

print(result)
```
