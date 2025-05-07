# ListPackagesOkResponse

**Properties**

| Name         | Type           | Required | Description                                                                                                                                                                                                                                                                                    |
| :----------- | :------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| packages     | List[Packages] | ❌       |                                                                                                                                                                                                                                                                                                |
| after_cursor | str            | ❌       | The cursor value representing the end of the current page of results. Use this cursor value as the "afterCursor" parameter in your next request to retrieve the subsequent page of results. It ensures that you continue fetching data from where you left off, facilitating smooth pagination |

# Packages

**Properties**

| Name                | Type  | Required | Description                                                                                                                                                                 |
| :------------------ | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                | str   | ❌       | ID of the package                                                                                                                                                           |
| destination         | str   | ❌       | ISO representation of the package's destination.                                                                                                                            |
| data_limit_in_bytes | float | ❌       | Size of the package in bytes. For **limited packages**, this field will return the data limit in bytes. For **unlimited packages**, it will return **-1** as an identifier. |
| min_days            | float | ❌       | Min number of days for the package                                                                                                                                          |
| max_days            | float | ❌       | Max number of days for the package                                                                                                                                          |
| price_in_cents      | float | ❌       | Price of the package in cents                                                                                                                                               |
