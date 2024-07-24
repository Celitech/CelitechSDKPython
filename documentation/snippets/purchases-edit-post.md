```python
from celitech import Celitech, Environment
from celitech.models import EditPurchaseRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
)

request_body = EditPurchaseRequest(
    purchase_id="ae471106-c8b4-42cf-b83a-b061291f2922",
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.edit_purchase(request_body=request_body)

print(result)

```