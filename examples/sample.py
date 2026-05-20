from celitech import Celitech

sdk = Celitech(client_id="CLIENT_ID", client_secret="CLIENT_SECRET")

result = sdk.destinations.list_destinations(accept="application/json")

print(result)
