# RandomDog API
# URL: https://random.dog

import re
import json
import requests

url = "https://random.dog/woof.json"
response = requests.get(url)
data = response.json()
with open("./API/RandomDog/woof.json", "w") as file:
    json.dump(data, file, indent = 4)

dog_url = data["url"]
# 獲取檔案的副檔名
extension = re.search(r"\.([^.]+)$", dog_url).group(1)
# 檔案大小格式化
dog_filesize = data["fileSizeBytes"] / 1024
if dog_filesize < 1024:
    dog_filesize = f"{dog_filesize:.3f}kb"
else:
    dog_filesize = f"{dog_filesize / 1024:.3f}mb"

dog_response = requests.get(dog_url)
with open(f"./API/RandomDog/dog.{extension}", "wb") as file:
    file.write(dog_response.content)

print(f"url: {dog_url}, size: {dog_filesize}")
