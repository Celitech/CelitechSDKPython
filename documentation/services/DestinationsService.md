# DestinationsService

A list of all methods in the `DestinationsService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description       |
| :-------------------------------------- | :---------------- |
| [list_destinations](#list_destinations) | List Destinations |

## list_destinations

List Destinations

- HTTP Method: `GET`
- Endpoint: `/destinations`

**Return Type**

`ListDestinationsOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

result = sdk.destinations.list_destinations()

print(result)
```
