# ListPurchasesOkResponse

**Properties**

| Name         | Type            | Required | Description                                                                                                                                                                                                                                                                                     |
| :----------- | :-------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| purchases    | List[Purchases] | ❌       |                                                                                                                                                                                                                                                                                                 |
| after_cursor | str             | ❌       | The cursor value representing the end of the current page of results. Use this cursor value as the "afterCursor" parameter in your next request to retrieve the subsequent page of results. It ensures that you continue fetching data from where you left off, facilitating smooth pagination. |

# Purchases

**Properties**

| Name         | Type          | Required | Description                                                                                                                                                                                                               |
| :----------- | :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_         | str           | ❌       | ID of the purchase                                                                                                                                                                                                        |
| start_date   | str           | ❌       | Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'                                                                                                                                                |
| end_date     | str           | ❌       | End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'                                                                                                                                                  |
| created_date | str           | ❌       | Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'                                                                                                                                                       |
| start_time   | float         | ❌       | Epoch value representing the start time of the package's validity                                                                                                                                                         |
| end_time     | float         | ❌       | Epoch value representing the end time of the package's validity                                                                                                                                                           |
| created_at   | float         | ❌       | Epoch value representing the date of creation of the purchase                                                                                                                                                             |
| package      | Package       | ❌       |                                                                                                                                                                                                                           |
| esim         | PurchasesEsim | ❌       |                                                                                                                                                                                                                           |
| source       | str           | ❌       | The source indicates where the eSIM was purchased, which can be from the API, dashboard, landing-page, promo-page or iframe. For purchases made before September 8, 2023, the value will be displayed as 'Not available'. |
| reference_id | str           | ❌       | The referenceId that was provided by the partner during the purchase or topup flow. This identifier can be used for analytics and debugging purposes.                                                                     |

# Package

**Properties**

| Name                | Type  | Required | Description                                     |
| :------------------ | :---- | :------- | :---------------------------------------------- |
| id\_                | str   | ❌       | ID of the package                               |
| data_limit_in_bytes | float | ❌       | Size of the package in Bytes                    |
| destination         | str   | ❌       | ISO representation of the package's destination |
| destination_name    | str   | ❌       | Name of the package's destination               |
| price_in_cents      | float | ❌       | Price of the package in cents                   |

# PurchasesEsim

**Properties**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ❌       | ID of the eSIM |

<!-- This file was generated by liblab | https://liblab.com/ -->
