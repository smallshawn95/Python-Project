import requests

url = "https://smallshawn95.github.io/"
short_url = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
print(short_url.text)
print(short_url.content.decode("utf-8"))
