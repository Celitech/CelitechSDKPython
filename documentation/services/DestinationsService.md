# DestinationsService

A list of all methods in the `DestinationsService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description              |
| :-------------------------------------- | :----------------------- |
| [list_destinations](#list_destinations) | Name of the destinations |

## list_destinations

Name of the destinations

- HTTP Method: `GET`
- Endpoint: `/destinations`

**Return Type**

`ListDestinationsOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech, Environment

sdk = Celitech(
    base_url=Environment.DEFAULT.value
)

result = sdk.destinations.list_destinations()

print(result)
```
