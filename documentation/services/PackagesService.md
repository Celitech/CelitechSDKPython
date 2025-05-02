# PackagesService

A list of all methods in the `PackagesService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description   |
| :------------------------------ | :------------ |
| [list_packages](#list_packages) | List Packages |

## list_packages

List Packages

- HTTP Method: `GET`
- Endpoint: `/packages`

**Parameters**

| Name             | Type  | Required | Description                                                                                                                                                                                                         |
| :--------------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| destination      | str   | ❌       | ISO representation of the package's destination.                                                                                                                                                                    |
| start_date       | str   | ❌       | Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.                                                                      |
| end_date         | str   | ❌       | End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.                                                                                                    |
| data_limit_in_gb | float | ❌       | Size of the package in GB. - **Limited Packages (1, 2, 3, 5, 8, 20GB) - **Unlimited Packages (Region-3 only):** Use **-1\*\* for unlimited.                                                                         |
| after_cursor     | str   | ❌       | To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data. |
| limit            | float | ❌       | Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20                                                 |
| start_time       | int   | ❌       | Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months                                                              |
| end_time         | int   | ❌       | Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time                                                                                                   |
| duration         | float | ❌       | Duration in seconds for the package's validity. If this parameter is present, it will override the startTime and endTime parameters. The maximum duration for a package's validity period is 90 days                |

**Return Type**

`ListPackagesOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.packages.list_packages()

print(result)
```
