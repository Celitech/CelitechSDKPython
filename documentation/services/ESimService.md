# ESimService

A list of all methods in the `ESimService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                            |
| :------------------------------------ | :------------------------------------- |
| [get_esim](#get_esim)                 | Get status from eSIM                   |
| [get_esim_device](#get_esim_device)   | Get device info from an installed eSIM |
| [get_esim_history](#get_esim_history) | Get history from an eSIM               |
| [get_esim_mac](#get_esim_mac)         | Get MAC from eSIM                      |

## get_esim

Get status from eSIM

- HTTP Method: `GET`
- Endpoint: `/esim`

**Parameters**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ✅       | ID of the eSIM |

**Return Type**

`GetEsimOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech, Environment

sdk = Celitech(
    base_url=Environment.DEFAULT.value
)

result = sdk.e_sim.get_esim(iccid="1111222233334444555")

print(result)
```

## get_esim_device

Get device info from an installed eSIM

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/device`

**Parameters**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ✅       | ID of the eSIM |

**Return Type**

`GetEsimDeviceOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech, Environment

sdk = Celitech(
    base_url=Environment.DEFAULT.value
)

result = sdk.e_sim.get_esim_device(iccid="1111222233334444555")

print(result)
```

## get_esim_history

Get history from an eSIM

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/history`

**Parameters**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ✅       | ID of the eSIM |

**Return Type**

`GetEsimHistoryOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech, Environment

sdk = Celitech(
    base_url=Environment.DEFAULT.value
)

result = sdk.e_sim.get_esim_history(iccid="1111222233334444555")

print(result)
```

## get_esim_mac

Get MAC from eSIM

- HTTP Method: `GET`
- Endpoint: `/esim/{iccid}/mac`

**Parameters**

| Name  | Type | Required | Description    |
| :---- | :--- | :------- | :------------- |
| iccid | str  | ✅       | ID of the eSIM |

**Return Type**

`GetEsimMacOkResponse`

**Example Usage Code Snippet**

```python
from celitech import Celitech, Environment

sdk = Celitech(
    base_url=Environment.DEFAULT.value
)

result = sdk.e_sim.get_esim_mac(iccid="1111222233334444555")

print(result)
```
