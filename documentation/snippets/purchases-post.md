```python
from celitech import Celitech
from celitech.models import CreatePurchaseRequest

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = CreatePurchaseRequest(
    destination="FRA",
    data_limit_in_gb=1,
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.create_purchase(request_body=request_body)

print(result)

```
