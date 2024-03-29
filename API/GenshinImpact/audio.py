import requests

# 官方文檔: https://api.pearktrue.cn/info?id=230
api = "https://api.pearktrue.cn/api/genshinimpactaudio/"
text = "原神，啟動！"
speaker = "派蒙"

response = requests.get(f"{api}?text={text}&speaker={speaker}")
genshin_impact = response.json()
print(genshin_impact)

with open("./API/GenshinImpact/audio.wav", "wb") as file:
    audio = requests.get(genshin_impact["audiourl"])
    file.write(audio.content)
