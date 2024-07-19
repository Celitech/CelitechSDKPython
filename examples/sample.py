from celitech import Celitech, Environment

sdk = Celitech(
    client_id="client-id",
    client_secret="client-secret",
    base_url=Environment.DEFAULT.value,
)

result = sdk.destinations.list_destinations()

print(result)
