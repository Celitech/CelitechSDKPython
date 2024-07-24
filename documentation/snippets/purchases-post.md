```python
from celitech import Celitech, Environment
from celitech.models import CreatePurchaseRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
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
