```python
from celitech import Celitech
from celitech.models import TopUpEsimRequest

sdk = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET"
)

request_body = TopUpEsimRequest(
    iccid="1111222233334444555000",
    data_limit_in_gb=1,
    start_date="2023-11-01",
    end_date="2023-11-20"
)

result = sdk.purchases.top_up_esim(request_body=request_body)

print(result)

```
