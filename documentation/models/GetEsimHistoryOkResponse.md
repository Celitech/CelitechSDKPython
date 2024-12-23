# GetEsimHistoryOkResponse

**Properties**

| Name | Type                         | Required | Description |
| :--- | :--------------------------- | :------- | :---------- |
| esim | GetEsimHistoryOkResponseEsim | ❌       |             |

# GetEsimHistoryOkResponseEsim

**Properties**

| Name    | Type          | Required | Description    |
| :------ | :------------ | :------- | :------------- |
| iccid   | str           | ❌       | ID of the eSIM |
| history | List[History] | ❌       |                |

# History

**Properties**

| Name        | Type  | Required | Description                                                                                                                         |
| :---------- | :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| status      | str   | ❌       | The status of the eSIM at a given time, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR' |
| status_date | str   | ❌       | The date when the eSIM status changed in the format 'yyyy-MM-ddThh:mm:ssZZ'                                                         |
| date\_      | float | ❌       | Epoch value representing the date when the eSIM status changed                                                                      |
