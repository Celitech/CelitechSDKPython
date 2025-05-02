```python
from celitech import Celitech
from celitech.models import CreatePurchaseV2Request

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = CreatePurchaseV2Request(
    destination="FRA",
    data_limit_in_gb=1,
    quantity=1
)

result = sdk.purchases.create_purchase_v2(request_body=request_body)

print(result)

```
