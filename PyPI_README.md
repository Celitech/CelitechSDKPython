# Celitech Python SDK 2.0.9<a id="celitech-python-sdk-209"></a>

Welcome to the Celitech SDK documentation. This guide will help you get started with integrating and using the Celitech SDK in your project.

## Versions<a id="versions"></a>

- API version: `2.0.9`
- SDK version: `2.0.9`

## About the API<a id="about-the-api"></a>

Welcome to the CELITECH API documentation!

Useful links: [Homepage](https://www.celitech.com) | [Support email](mailto:devops@celitech.com) | [Blog](https://www.celitech.com/blog/)

# Introduction

This is the reference documentation and schemas for the CELITECH API and webhooks. For tutorials and other documentation please refer to the [CELITECH Documentation](https://docs.celitech.com).

"Partners" refers to online service providers that use our eSIM API. Access levels include Gold, Platinum, and Diamond.

## API

The CELITECH API is designed for use by partner platforms, including both web and mobile applications. It's assumed all endpoint calls are initiated from the backend of an integrated platform.

API URL: `https://api.celitech.net/v1`

## Authentication & Authorization

CELITECH API uses the OAuth 2.0 protocol for authentication and authorization.
The endpoints are protected using client credentials flow which is based on a token exchange. The token has a defined life span (typically 1 hour), after which a new token must be obtained.

To begin, obtain OAuth 2.0 client credentials ( **CLIENT_ID** & **CLIENT_SECRET** ) from the [CELITECH Dashboard](https://www.dashboard.celitech.com/). Then your client application requests an access token from the CELITECH Authorization Server, extracts a token from the response, and sends the token to the CELITECH API that you want to access.

Security Scheme Type: `OAuth2`

Flow type: `clientCredentials`

Token URL: `https://auth.celitech.net/oauth2/token`

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [OAuth Authentication](#oauth-authentication)
  - [Environment Variables](#environment-variables)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
- [License](#license)

# Setup & Configuration<a id="setup--configuration"></a>

## Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.9`

## Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install celitech-sdk
```

If you are using Python 3, you can use `pip3` instead:

```bash
pip3 install celitech-sdk
```

## Disabling Redirects<a id="disabling-redirects"></a>

By default, the SDK follows HTTP redirects (3xx responses) automatically. Pass
`follow_redirects=False` to get the redirect response back as-is instead:

```python
client = Celitech(follow_redirects=False)
```

This can also be changed later with `client.set_follow_redirects(False)`.

## Logging<a id="logging"></a>

The SDK is silent by default. Pass a standard library `logging.Logger` as `logger` to log
every outgoing request and its response (method, URL, status, and duration):

```python
import logging

logger = logging.getLogger("Celitech")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

client = Celitech(logger=logger)
```

This can also be changed later with `client.set_logging(logger)`.

`Authorization` and `Cookie` header values are always redacted in logged output, regardless
of the logger's own configuration.

## Authentication<a id="authentication"></a>

### OAuth Authentication<a id="oauth-authentication"></a>

The Celitech API uses OAuth 2.0 for authentication.

You need to provide your OAuth credentials when initializing the SDK. Tokens are automatically fetched, cached, and refreshed — you do not need to manage them yourself.

```py
sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)
```

If you need to set or update the OAuth credentials after the SDK initialization, you can use:

```py
sdk.set_client_id("CLIENT_ID")
sdk.set_client_secret("CLIENT_SECRET")
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

sdk = Celitech(timeout=10)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.destinations.list_destinations()

print(result)

```

# Async Usage<a id="async-usage"></a>

The SDK includes an Async Client for making asynchronous API requests. This is useful for applications that need non-blocking operations, like web servers or apps with a graphical user interface.

```py
import asyncio
from celitech import CelitechAsync

sdk = CelitechAsync(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)


async def main():
  result = await sdk.destinations.list_destinations()
  print(result)

asyncio.run(main())
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
| i_frame      |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                             | Description |
| :------------------------------- | :---------- |
| ListDestinationsOkResponse       |             |
| ListPackagesOkResponse           |             |
| CreatePurchaseV2Request          |             |
| CreatePurchaseV2OkResponse       |             |
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
| SuspendEsimOkResponse            |             |
| TokenOkResponse                  |             |
| GrantType                        |             |
| ErrorResponse                    |             |

</details>

## License<a id="license"></a>

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.
