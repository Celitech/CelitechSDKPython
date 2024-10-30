```python
from celitech import Celitech

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret"
)

result = sdk.e_sim.get_esim_device(iccid="1111222233334444555000")

print(result)

```
