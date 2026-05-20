# EditService

A list of all methods in the `EditService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [edit_purchase](#edit_purchase) | This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits. |

## edit_purchase

This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

- HTTP Method: `POST`
- Endpoint: `/purchases/edit`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [EditPurchaseRequest](../models/EditPurchaseRequest.md) | ✅       | The request body. |
| accept       | str                                                     | ✅       |                   |

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

result = sdk.edit.edit_purchase(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
