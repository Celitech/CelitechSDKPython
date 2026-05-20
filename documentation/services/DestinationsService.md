# DestinationsService

A list of all methods in the `DestinationsService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description       |
| :-------------------------------------- | :---------------- |
| [list_destinations](#list_destinations) | List Destinations |

## list_destinations

List Destinations

- HTTP Method: `GET`
- Endpoint: `/destinations`

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

result = sdk.destinations.list_destinations(accept="application/json")

print(result)
```
