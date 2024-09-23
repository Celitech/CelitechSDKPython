# Celitech Python SDK 1.1.87<a id="celitech-python-sdk-1187"></a>

Welcome to the Celitech SDK documentation. This guide will help you get started with integrating and using the Celitech SDK in your project.

## Versions<a id="versions"></a>

- API version: `1.1.0`
- SDK version: `1.1.87`

## About the API<a id="about-the-api"></a>

Welcome to the CELITECH API documentation! Useful links: [Homepage](https://www.celitech.com) | [Support email](mailto:support@celitech.com) | [Blog](https://www.celitech.com/blog/)

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration<a id="setup--configuration"></a>

### Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install celitech-sdk
```

## Environment Variables<a id="environment-variables"></a>

These are the environment variables for the SDK:

| Name          | Description             |
| :------------ | :---------------------- |
| CLIENT_ID     | Client ID parameter     |
| CLIENT_SECRET | Client Secret parameter |

Environment variables are a way to configure your application outside the code. You can set these environment variables on the command line or use your project's existing tooling for managing environment variables.

If you are using a `.env` file, a template with the variable names is provided in the `.env.example` file located in the same directory as this README.

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from celitech import Celitech

sdk = Celitech(timeout=10000)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from celitech import Celitech, Environment

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
)

result = sdk.destinations.list_destinations()

print(result)

```

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name         |
| :----------- |
| destinations |
| packages     |
| purchases    |
| e_sim        |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                             | Description |
| :------------------------------- | :---------- |
| ListDestinationsOkResponse       |             |
| ListPackagesOkResponse           |             |
| ListPurchasesOkResponse          |             |
| CreatePurchaseRequest            |             |
| CreatePurchaseOkResponse         |             |
| TopUpEsimRequest                 |             |
| TopUpEsimOkResponse              |             |
| EditPurchaseRequest              |             |
| EditPurchaseOkResponse           |             |
| GetPurchaseConsumptionOkResponse |             |
| GetEsimOkResponse                |             |
| GetEsimDeviceOkResponse          |             |
| GetEsimHistoryOkResponse         |             |
| GetEsimMacOkResponse             |             |

</details>

## License<a id="license"></a>

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.