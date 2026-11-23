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

[`ListDestinationsResponse`](../models/ListDestinationsResponse.md)

**Example Usage Code Snippet**

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
result = client.destinations.list_destinations()

print(result)
```
