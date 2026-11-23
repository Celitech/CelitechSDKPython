# Reference

## DestinationsClient

<details><summary><code>client.destinations.list_destinations(...)</code></summary>

`GET /destinations`

List Destinations

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.destinations.list_destinations()
```

</details>

## PackagesClient

<details><summary><code>client.packages.list_packages(...)</code></summary>

`GET /packages`

List Packages

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.packages.list_packages()
```

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

</details>

## PurchasesClient

<details><summary><code>client.purchases.create_purchase_v2(...)</code></summary>

`POST /purchases/v2`

Create Purchase V2

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.purchases.create_purchase_v2(
    destination="FRA",
    data_limit_in_gb=1,
    quantity=1,
)
```

**Parameters:**

- `idempotency_key`

</details>

<details><summary><code>client.purchases.list_purchases(...)</code></summary>

`GET /purchases`

List Purchases

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.purchases.list_purchases()
```

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

</details>

<details><summary><code>client.purchases.create_purchase(...)</code></summary>

`POST /purchases`

Create Purchase

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.purchases.create_purchase(
    destination="FRA",
    data_limit_in_gb=1,
    start_date="2023-11-01",
    end_date="2023-11-20",
)
```

**Parameters:**

- `idempotency_key`

</details>

<details><summary><code>client.purchases.top_up_esim(...)</code></summary>

`POST /purchases/topup`

Top-up eSIM

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.purchases.top_up_esim(
    iccid="1111222233334444555000",
    data_limit_in_gb=1,
)
```

**Parameters:**

- `idempotency_key`

</details>

<details><summary><code>client.purchases.edit_purchase(...)</code></summary>

`POST /purchases/edit`

Edit Purchase

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.purchases.edit_purchase(
    purchase_id="ae471106-c8b4-42cf-b83a-b061291f2922",
    start_date="2023-11-01",
    end_date="2023-11-20",
)
```

**Parameters:**

- `idempotency_key`

</details>

<details><summary><code>client.purchases.get_purchase_consumption(...)</code></summary>

`GET /purchases/{purchaseId}/consumption`

Get Purchase Consumption

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.purchases.get_purchase_consumption(
    purchase_id="4973fa15-6979-4daa-9cf3-672620df819c",
)
```

**Parameters:**

- `purchase_id` (required)

</details>

## ESimClient

<details><summary><code>client.e_sim.get_esim(...)</code></summary>

`GET /esim`

Get eSIM

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.e_sim.get_esim(
    iccid="1111222233334444555000",
)
```

**Parameters:**

- `iccid` (required)

</details>

<details><summary><code>client.e_sim.get_esim_device(...)</code></summary>

`GET /esim/{iccid}/device`

Get eSIM Device

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.e_sim.get_esim_device(
    iccid="1111222233334444555000",
)
```

**Parameters:**

- `iccid` (required)

</details>

<details><summary><code>client.e_sim.get_esim_history(...)</code></summary>

`GET /esim/{iccid}/history`

Get eSIM History

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.e_sim.get_esim_history(
    iccid="1111222233334444555000",
)
```

**Parameters:**

- `iccid` (required)

</details>

<details><summary><code>client.e_sim.suspend_esim(...)</code></summary>

`POST /esim/{iccid}/suspend`

Suspend eSIM

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.e_sim.suspend_esim(
    iccid="1111222233334444555000",
)
```

**Parameters:**

- `iccid` (required)
- `idempotency_key`

</details>

## IFrameClient

<details><summary><code>client.i_frame.token(...)</code></summary>

`POST /iframe/token`

Generate Token

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.i_frame.token()
```

</details>

## OAuthClient

<details><summary><code>client.o_auth.get_access_token_(...)</code></summary>

`POST /oauth2/token`

#### 🔌 Usage

```python
from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.o_auth.get_access_token_(
    grant_type="client_credentials",
    client_id="your_client_id",
    client_secret="your_client_secret",
    scope="read write",
)
```

</details>
