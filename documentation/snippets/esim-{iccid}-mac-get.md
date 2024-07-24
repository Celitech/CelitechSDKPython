```python
from celitech import Celitech, Environment

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
)

result = sdk.e_sim.get_esim_mac(iccid="1111222233334444555")

print(result)

```