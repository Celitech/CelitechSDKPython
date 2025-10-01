# GetEsimOkResponse

**Properties**

| Name | Type                  | Required | Description |
| :--- | :-------------------- | :------- | :---------- |
| esim | GetEsimOkResponseEsim | ❌       |             |

# GetEsimOkResponseEsim

**Properties**

| Name                   | Type | Required | Description                                                                                                                    |
| :--------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------- |
| iccid                  | str  | ❌       | ID of the eSIM                                                                                                                 |
| smdp_address           | str  | ❌       | SM-DP+ Address                                                                                                                 |
| manual_activation_code | str  | ❌       | The manual activation code                                                                                                     |
| status                 | str  | ❌       | Status of the eSIM, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'                |
| is_top_up_allowed      | bool | ❌       | Indicates whether the eSIM is currently eligible for a top-up. This flag should be checked before attempting a top-up request. |
