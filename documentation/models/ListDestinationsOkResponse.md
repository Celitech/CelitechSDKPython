# ListDestinationsOkResponse

**Properties**

| Name         | Type               | Required | Description |
| :----------- | :----------------- | :------- | :---------- |
| destinations | List[Destinations] | ❌       |             |

# Destinations

**Properties**

| Name                | Type      | Required | Description                           |
| :------------------ | :-------- | :------- | :------------------------------------ |
| name                | str       | ❌       | Name of the destination               |
| destination         | str       | ❌       | ISO representation of the destination |
| supported_countries | List[str] | ❌       |                                       |
