import json

with open("pygments.json", "r", encoding = "utf8") as file:
    data = json.load(file)

lexers = {}
for lexer in data["lexers"]:
    lexer = lexer[0].title()
    if lexer[0] not in lexers:
        lexers[lexer[0]] = []
    lexers[lexer[0]].append(lexer)

for char in lexers:
    lexers[char].sort()

print(lexers)
