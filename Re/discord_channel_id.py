import re

channel_mention = "<#1021706869724684376>"

match = re.match("<#(\d+)>", channel_mention)

if match:
    channel_id = match.group(1)
    print(f"符合格式，頻道ID為: {channel_id}")
else:
    print("不符合格式")
