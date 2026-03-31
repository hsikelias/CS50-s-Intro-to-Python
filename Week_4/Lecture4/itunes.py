import json
import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

# now we use python as a web browser to get data from the website

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])
# pretty much a dictionary, bunch of key and value pairs, a dictionary can be inside a dictionary
