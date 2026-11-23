# GetEsimDeviceResponse

**Properties**

| Name   | Type                                                        | Required | Description |
| :----- | :---------------------------------------------------------- | :------- | :---------- |
| device | [GetEsimDeviceResponseDevice](#getesimdeviceresponsedevice) | ✅        |             |

# GetEsimDeviceResponseDevice

**Properties**

| Name           | Type | Required | Description               |
| :------------- | :--- | :------- | :------------------------ |
| oem            | str  | ✅        | Name of the OEM           |
| hardware_name  | str  | ✅        | Name of the Device        |
| hardware_model | str  | ✅        | Model of the Device       |
| eid            | str  | ✅        | Serial Number of the eSIM |
