# Reference

## DestinationsClient

### `client.destinations.list_destinations`

`GET /destinations`

List Destinations

## PackagesClient

### `client.packages.list_packages`

`GET /packages`

List Packages

**Parameters:**

- `destination`
- `data_limit_in_gb`
- `start_date`
- `end_date`
- `after_cursor`
- `limit`
- `start_time`
- `end_time`
- `include_unlimited`

## PurchasesClient

### `client.purchases.create_purchase_v2`

`POST /purchases/v2`

Create Purchase V2

**Parameters:**

- `idempotency_key`

### `client.purchases.list_purchases`

`GET /purchases`

List Purchases

**Parameters:**

- `purchase_id`
- `iccid`
- `after_date`
- `before_date`
- `email`
- `reference_id`
- `after_cursor`
- `limit`
- `after`
- `before`

### `client.purchases.create_purchase`

`POST /purchases`

Create Purchase

**Parameters:**

- `idempotency_key`

### `client.purchases.top_up_esim`

`POST /purchases/topup`

Top-up eSIM

**Parameters:**

- `idempotency_key`

### `client.purchases.edit_purchase`

`POST /purchases/edit`

Edit Purchase

**Parameters:**

- `idempotency_key`

### `client.purchases.get_purchase_consumption`

`GET /purchases/{purchaseId}/consumption`

Get Purchase Consumption

**Parameters:**

- `purchase_id` (required)

## ESimClient

### `client.e_sim.get_esim`

`GET /esim`

Get eSIM

**Parameters:**

- `iccid` (required)

### `client.e_sim.get_esim_device`

`GET /esim/{iccid}/device`

Get eSIM Device

**Parameters:**

- `iccid` (required)

### `client.e_sim.get_esim_history`

`GET /esim/{iccid}/history`

Get eSIM History

**Parameters:**

- `iccid` (required)

### `client.e_sim.suspend_esim`

`POST /esim/{iccid}/suspend`

Suspend eSIM

**Parameters:**

- `iccid` (required)
- `idempotency_key`

## IFrameClient

### `client.i_frame.token`

`POST /iframe/token`

Generate Token

## OAuthClient

### `client.o_auth.get_access_token_`

`POST /oauth2/token`
