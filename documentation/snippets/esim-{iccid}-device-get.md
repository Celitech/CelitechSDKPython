```python
from celitech import Celitech

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

result = sdk.e_sim.get_esim_device(iccid="1111222233334444555000")

print(result)

```
