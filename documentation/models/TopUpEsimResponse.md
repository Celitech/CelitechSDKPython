# TopUpEsimResponse

**Properties**

| Name     | Type                                                    | Required | Description |
| :------- | :------------------------------------------------------ | :------- | :---------- |
| purchase | [TopUpEsimResponsePurchase](#topupesimresponsepurchase) | ✅        |             |
| profile  | [TopUpEsimResponseProfile](#topupesimresponseprofile)   | ✅        |             |

# TopUpEsimResponsePurchase

**Properties**

| Name         | Type  | Required | Description                                                                |
| :----------- | :---- | :------- | :------------------------------------------------------------------------- |
| id           | str   | ✅        | ID of the purchase                                                         |
| package_id   | str   | ✅        | ID of the package                                                          |
| start_date   | str   | ✅        | Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ' |
| end_date     | str   | ✅        | End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'   |
| created_date | str   | ✅        | Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'        |
| start_time   | float | ❌        | Epoch value representing the start time of the package's validity          |
| end_time     | float | ❌        | Epoch value representing the end time of the package's validity            |

# TopUpEsimResponseProfile

**Properties**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ✅        | ID of the eSIM |
