import requests

text = "原神，啟動！"
response = requests.get(f"https://api.pearktrue.cn/api/genshinimpactaudio/?text={text}&speaker=八重神子")
if response.status_code == 200:
    data = response.json()
    print(data)
    voice = requests.get(data["audiourl"])
    with open("genshin_impact.mp3", "wb") as file:
        file.write(voice.content)
