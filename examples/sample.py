from celitech import Celitech

client = Celitech(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
client.destinations.list_destinations()
