import json, requests
from bs4 import BeautifulSoup

problem_dict = {}
html = requests.get("https://cses.fi/problemset/")
soup = BeautifulSoup(html.content, "html.parser")
h2s = soup.find_all("h2")
uls = soup.find_all("ul", class_ = "task-list")
for i in range(1, len(h2s)):
    problem_dict[h2s[i].text] = {}
    lis = uls[i].find_all("li")
    for j in range(len(lis)):
        a = lis[j].find("a")
        span = lis[j].find("span", class_ = "detail")
        problem_dict[h2s[i].text][a.text] = {
            "url": f"https://cses.fi{a.get('href')}",
            "people": span.text
        }

with open("./cses.json", "w", encoding = "utf8") as file:
    json.dump(problem_dict, file, indent = 4, ensure_ascii = False)
