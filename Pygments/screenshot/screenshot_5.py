import json

with open("pygments.json", "r", encoding = "utf8") as file:
    data = json.load(file)

lexers = []
for lexer in data["lexers"]:
    if " " not in lexer[0].title():
        lexers.append(lexer[0].title())
lexers.sort()

x = 1
s = set()
text = ""
for lexer in lexers:
    if lexer[0] not in s:
        x = 0
        s.add(lexer[0])
        text += f"\n{lexer[0]}:\n"
    elif x % 5 == 0:
        text += "\n"
    x += 1
    text += f"{lexer} "

print(text)