# GetAccessTokenRequest

**Properties**

| Name          | Type      | Required | Description |
| :------------ | :-------- | :------- | :---------- |
| grant_type    | GrantType | ❌       |             |
| client_id     | str       | ❌       |             |
| client_secret | str       | ❌       |             |

# GrantType

**Properties**

| Name              | Type | Required | Description          |
| :---------------- | :--- | :------- | :------------------- |
| CLIENTCREDENTIALS | str  | ✅       | "client_credentials" |
