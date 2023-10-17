import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.dgpa.gov.tw/typh/daily/nds.html")
response.encoding = "utf8"

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("div", class_ = "Header_YMD")
print("".join(title.text.split()))

update_time = soup.find("h4")
print(" ".join(update_time.text.split()[0:2]))

table = soup.find("table", id = "Table")
tbody = table.find("tbody", class_ = "Table_Body")
trs = tbody.find_all("tr")
del trs[-1]
num = 0
for tr in trs:
    num += 1
    city_name = tr.find("td")
    stop_info = city_name.find_next("td")
    print(str(num).zfill(2), city_name.text, stop_info.text)
