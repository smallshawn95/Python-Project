import json
import pprint
import requests

url = "https://cataas.com/api/tags"
response = requests.get(url)
data = response.json()

pprint.pprint(data)

tags_data = {
    "tags": [tag for tag in data if tag]
}

with open("./API/CATAAS/tags.json", "w", encoding = "utf8") as file:
    json.dump(tags_data, file, indent = 4, ensure_ascii = False)
