from celitech import Celitech, Environment

sdk = Celitech(base_url=Environment.DEFAULT.value)

result = sdk.destinations.list_destinations()

print(result)
