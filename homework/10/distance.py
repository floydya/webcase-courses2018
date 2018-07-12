from urllib.parse import urlencode
from urllib.request import urlopen
import json


params = urlencode({"origins": input("Otkuda: "), "destinations": input("Kuda: ")})
response = urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?" + params).read()
result = json.loads(response)
print("Rasstoyanie: " + str(result.get("rows")[0].get("elements")[0].get("distance").get("text")))
