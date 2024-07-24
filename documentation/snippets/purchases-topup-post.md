```python
from celitech import Celitech, Environment
from celitech.models import TopUpEsimRequest

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value
)

request_body = TopUpEsimRequest(
    iccid="1111222233334444555",
    data_limit_in_gb=1,
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.top_up_esim(request_body=request_body)

print(result)

```
