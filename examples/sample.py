from celitech import Celitech

sdk = Celitech(client_id="CLIENT_ID", client_secret="CLIENT_SECRET", timeout=10000)

result = sdk.destinations.list_destinations()

print(result)
