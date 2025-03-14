# CreatePurchaseV2OkResponse

**Properties**

| Name     | Type                               | Required | Description |
| :------- | :--------------------------------- | :------- | :---------- |
| purchase | CreatePurchaseV2OkResponsePurchase | ❌       |             |
| profile  | CreatePurchaseV2OkResponseProfile  | ❌       |             |

# CreatePurchaseV2OkResponsePurchase

**Properties**

| Name         | Type | Required | Description                                                         |
| :----------- | :--- | :------- | :------------------------------------------------------------------ |
| id\_         | str  | ❌       | ID of the purchase                                                  |
| package_id   | str  | ❌       | ID of the package                                                   |
| created_date | str  | ❌       | Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ' |

# CreatePurchaseV2OkResponseProfile

**Properties**

| Name            | Type | Required | Description    |
| :-------------- | :--- | :------- | :------------- |
| iccid           | str  | ❌       | ID of the eSIM |
| activation_code | str  | ❌       |                |
