# GetEsimHistoryResponse

**Properties**

| Name | Type                                                      | Required | Description |
| :--- | :-------------------------------------------------------- | :------- | :---------- |
| esim | [GetEsimHistoryResponseEsim](#getesimhistoryresponseesim) | ✅        |             |

# GetEsimHistoryResponseEsim

**Properties**

| Name    | Type                                                                                  | Required | Description    |
| :------ | :------------------------------------------------------------------------------------ | :------- | :------------- |
| iccid   | str                                                                                   | ✅        | ID of the eSIM |
| history | [List[GetEsimHistoryResponseEsimHistoryItem]](#getesimhistoryresponseesimhistoryitem) | ✅        |                |

# GetEsimHistoryResponseEsimHistoryItem

**Properties**

| Name        | Type  | Required | Description                                                                                                                         |
| :---------- | :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| status      | str   | ✅        | The status of the eSIM at a given time, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR' |
| status_date | str   | ✅        | The date when the eSIM status changed in the format 'yyyy-MM-ddThh:mm:ssZZ'                                                         |
| date        | float | ❌        | Epoch value representing the date when the eSIM status changed                                                                      |
