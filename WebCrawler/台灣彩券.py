import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/index_new.aspx?aspxerrorpath=/index_news.aspx"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

Beautiful = "-" * 20
print(f"{Beautiful}\n【A】雙贏彩\n【B】威力彩\n【C】大樂透\n【D】3星彩\n【E】4星彩\n{Beautiful}")
c = input("輸入欲查詢彩券代號：")
print(Beautiful)

if c == "A":
    #雙贏彩號碼
    data = soup.find("div", class_ = "contents_box06")
    name = data.find("span", class_ = "font_black15").text
    print(f"雙贏彩 {name}")
    number = data.find_all("div", class_ = "ball_tx ball_blue")
    print("開出順序：", end = "")
    for i in range(12):
        print(number[i].text, end = " ")
    print("\n大小順序：", end = "")
    for i in range(12, 24):
        print(number[i].text, end = " ")
elif c == "B":
    #威力彩號碼
    data = soup.find_all("div", class_ = "contents_box02")
    name = data[0].find("span", class_ = "font_black15").text
    print(f"威力彩 {name}")
    number = data[0].find_all("div", class_ = "ball_tx ball_green")
    print("開出順序：", end = "")
    for i in range(6):
        print(number[i].text, end = " ")
    print("\n大小順序：", end = "")
    for i in range(6, 12):
        print(number[i].text, end = " ")
    print("\n第二區：" + data[0].find("div", class_="ball_red").text)
elif c == "C":
    #大樂透號碼
    data = soup.find_all("div", class_ = "contents_box02")
    name = data[2].find("span", class_ = "font_black15").text
    print(f"大樂透 {name}")
    number = data[2].find_all("div", class_ = "ball_tx ball_yellow")
    print("開出順序：", end = "")
    for i in range(6):
        print(number[i].text, end = " ")
    print("\n大小順序：", end = "")
    for i in range(6, 12):
        print(number[i].text, end = " ")
    print("\n特別號：" + data[2].find("div", class_="ball_red").text)
elif c == "D":
    #3星彩號碼
    data = soup.find_all("div", class_ = "contents_box04")
    name = data[0].find("span", class_ = "font_black15").text
    print(f"3星彩 {name}")
    number = data[0].find_all("div", class_ = "ball_tx ball_purple")
    print("中獎號碼：", end = "")
    for i in range(3):
        print(number[i].text, end = " ")
elif c == "E":
    #4星彩號碼
    data = soup.find_all("div", class_ = "contents_box04")
    name = data[1].find("span", class_ = "font_black15").text
    print(f"4星彩 {name}")
    number = data[1].find_all("div", class_ = "ball_tx ball_purple")
    print("中獎號碼：", end = "")
    for i in range(4):
        print(number[i].text, end = " ")
else:
    print("代碼並未匹配到彩券名稱，請重新輸入試試！")
