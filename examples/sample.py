from celitech import Celitech

sdk = Celitech(client_id="client-id", client_secret="client-secret")

result = sdk.destinations.list_destinations()

print(result)
