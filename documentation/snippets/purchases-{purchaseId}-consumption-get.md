```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.purchases.get_purchase_consumption(purchase_id="4973fa15-6979-4daa-9cf3-672620df819c")

print(result)

```
