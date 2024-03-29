import time, requests
from bs4 import BeautifulSoup

singer = input("Singer Name: ")
song = input("Song Name: ")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
url = f"https://mojim.com/{singer}.html?t1"
html = requests.get(url, headers = headers)
html.encoding = "utf8"
soup = BeautifulSoup(html.text, "html.parser")
title = soup.find("a", title = f"{singer} 歌詞")
time.sleep(1)
singer_url = f"https://mojim.com/{title.get('href')}"
singer_html = requests.get(singer_url, headers = headers)
singer_soup = BeautifulSoup(singer_html.text, "html.parser")
singer_name = singer_soup.find_all("a")
for i in singer_name:
    if i.text == song:
        song_url = f"https://mojim.com/{i.get('href')}"
        break
time.sleep(1)
song_html = requests.get(song_url)
song_soup = BeautifulSoup(song_html.text, "html.parser")
song_text = song_soup.find("dd", id = "fsZx3")
try:
    song_text.ol.extract()
except:
    pass
song_text = str(song_text).replace("<br/>", "\n")
song_text = song_text.replace('更多更詳盡歌詞 在 <a href="http://mojim.com">※ Mojim.com　魔鏡歌詞網 </a>', "", 1)
song_text = song_text.replace('<dd class="fsZx3" id="fsZx3">', "", 1)
song_text = song_text.replace("</dd>", "", 1)
index = song_text.find("[00:")
if index == -1:
    index = len(song_text)
print(index)
first_sing_text = "\n".join([i.strip() for i in song_text[:index].split('\n') if i.strip() != ""])
print(first_sing_text)
print('-' * 50)
second_sing_text = "\n".join([i.strip() for i in song_text[index:].split('\n') if i.strip() != ""])
print(second_sing_text)
