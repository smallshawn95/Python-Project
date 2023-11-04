import os, re, requests

filename = input()

with open(f"./WebCrawler/{filename}.md", "r", encoding = "utf8") as file:
    document = file.read()

if not os.path.exists("f./WebCrawler/{filename}"):
    os.makedirs(f"./WebCrawler/{filename}")

x = 0
for line in document.splitlines():
    match = re.search("(https://[\s\S]+?.png)", line)
    if match:
        image_url = match.group(1)
        print(image_url)
        with open(f"./WebCrawler/{filename}/{x:02}.png", "wb") as file:
            file.write(requests.get(image_url).content)
        x += 1
