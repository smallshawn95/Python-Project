import re, json

code_block = "```json\n{\"abc\": 0}\n```"

match = re.search("```json\n([\s\S]+?)\n```", code_block)

code = match.group(1)
try:
    json.loads(code)
    print(code)
except json.JSONDecodeError:
    print("Json 格式錯誤")
