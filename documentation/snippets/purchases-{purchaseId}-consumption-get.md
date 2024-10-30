```python
from celitech import Celitech

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

result = sdk.purchases.get_purchase_consumption(purchase_id="4973fa15-6979-4daa-9cf3-672620df819c")

print(result)

```
