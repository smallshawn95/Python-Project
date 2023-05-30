import json
from pygments import lexers
from pygments.styles import get_all_styles

data = {}

data["lexers"] = []
for lexer in lexers.get_all_lexers():
    data["lexers"].append(lexer)

data["styles"] = []
for style in get_all_styles():
    data["styles"].append(style)

with open("pygment.json", "w", encoding = "utf8") as file:
    json.dump(data, file, indent = 4, ensure_ascii = False)
