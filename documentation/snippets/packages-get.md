```python
from celitech import Celitech, Environment

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
)

result = sdk.packages.list_packages()

print(result)

```
