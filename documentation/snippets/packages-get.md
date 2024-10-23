```python
from celitech import Celitech

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

result = sdk.packages.list_packages()

print(result)

```
