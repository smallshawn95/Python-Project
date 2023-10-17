import json, requests

with open("./IdentityV/role.json", "r", encoding = "utf8") as file:
    data = json.load(file)

for type_name in ["求生者", "監管者"]:
    for role_name in data[type_name]:
        avatar_url = data[type_name][role_name]["頭像"]
        role_name = role_name.strip("\"")
        with open(f"./IdentityV/avatar/{type_name}/{role_name}.png", "wb") as file:
            file.write(requests.get(avatar_url).content)
