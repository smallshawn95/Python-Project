import re, requests
from bs4 import BeautifulSoup
from pylatexenc.latex2text import LatexNodes2Text

problem_data = {}
url = "https://cses.fi/problemset/task/2418"
problem_html = requests.get(url)
problem_soup = BeautifulSoup(problem_html.content, "html.parser")
div = problem_soup.find("div", class_ = "content")
response_text = [text for text in div.text.splitlines() if text]

index_num = [2]
try:
    index_num.append(response_text.index("Input"))
except:
    index_num.append(0)
try:
    index_num.append(response_text.index("Output"))
except:
    index_num.append(0)
try:
    index_num.append(response_text.index("Constraints"))
except:
    index_num.append(0)
try:
    index_num.append(response_text.index("Example"))
except:
    index_num.append(0)
index_num.append(len(response_text))

tags = ["statement", "input", "output", "constraints", "example"]
problem_data["time_limit"] = response_text[1]
problem_data["memory_limit"] = response_text[2]
for i in range(5):
    if tags[i] in problem_data and problem_data[tags[i]] == "No Data":
        continue
    elif index_num[i + 1] == 0:
        index_num[i + 1] = index_num[i]
        problem_data[tags[i]] = "{}".format('\n'.join(response_text[index_num[i] + 1:index_num[i + 2]]))
        problem_data[tags[i + 1]] = "No Data"
    else:
        problem_data[tags[i]] = "{}".format('\n'.join(response_text[index_num[i] + 1:index_num[i + 1]]))

for tag in problem_data:
    text = problem_data[tag]
    matches = re.findall(r"\$([^$]+)\$", text)
    for i in set(matches):
        text = text.replace(f"${i}$", f"**{i}**")
    latex = LatexNodes2Text().latex_to_text(text)
    problem_data[tag] = latex
    print(f"{tag}:\n{problem_data[tag]}")

image = problem_soup.find("img", class_ = "invertible")
if image:
    print(f"Image:\nhttps://cses.fi{image.get('src')}")
