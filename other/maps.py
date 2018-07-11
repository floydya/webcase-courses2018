
import json, urllib.request
from urllib.parse import urlencode

params = {"address": input("Input address: ")}
query = "https://maps.googleapis.com/maps/api/geocode/json?" + urlencode(params)
response = urllib.request.urlopen(query).read().decode("utf-8")
jsonr = json.loads(response)
print(jsonr.get("results")[0].get("formatted_address"))
