```python
from celitech import Celitech, Environment

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
)

result = sdk.e_sim.get_esim(iccid="1111222233334444555000")

print(result)

```
