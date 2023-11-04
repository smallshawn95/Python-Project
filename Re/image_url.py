import re

url = "https://i.imgur.com/OLyEyaU.png"

match = re.match("![](https://[\s\S]+?.png)", url)

if match:
    image_url = match.group(1)
    print(image_url)
else:
    print("Not found image url.")
