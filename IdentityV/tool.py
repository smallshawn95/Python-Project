import os, json

with open("./IdentityV/role.json", "r", encoding = "utf8") as file:
    data = json.load(file)

'''
# 新增求生者定位
for role_name in data["求生者"]:
    genre = input(f"{role_name}: ")
    data["求生者"][role_name]["定位"] = genre
'''

'''
# 全部角色對照
survivor = data["全部"]["求生者"]
for filename in os.listdir("./IdentityV/picture/求生者"):
    try:
        survivor.remove(filename[:-4])
    except:
        try:
            survivor.remove(f"\"{filename[:-4]}\"")
        except:
            pass
print(survivor)

hunter = data["全部"]["監管者"]
for filename in os.listdir("./IdentityV/picture/監管者"):
    try:
        hunter.remove(filename[:-4])
    except:
        try:
            hunter.remove(f"\"{filename[:-4]}\"")
        except:
            pass
print(hunter)
'''

'''
# 全部角色統計
data["全部"] = {}

survivor = []
for role_name in data["求生者"]:
    survivor.append(role_name)
data["全部"]["求生者"] = survivor

decipher = []
for role_name in data["求生者"]:
    if "破譯型" in data["求生者"][role_name]["定位"]:
        decipher.append(role_name)
data["全部"]["破譯型"] = decipher

contain = []
for role_name in data["求生者"]:
    if "牽制型" in data["求生者"][role_name]["定位"]:
        contain.append(role_name)
data["全部"]["牽制型"] = contain

rescue = []
for role_name in data["求生者"]:
    if "救援型" in data["求生者"][role_name]["定位"]:
        rescue.append(role_name)
data["全部"]["救援型"] = rescue

auxiliary = []
for role_name in data["求生者"]:
    if "輔助型" in data["求生者"][role_name]["定位"]:
        auxiliary.append(role_name)
data["全部"]["輔助型"] = auxiliary

hunter = []
for role_name in data["監管者"]:
    hunter.append(role_name)
data["全部"]["監管者"] = hunter
'''

with open("./IdentityV/role.json", "w", encoding = "utf8") as file:
    json.dump(data, file, indent = 4, ensure_ascii = False)
