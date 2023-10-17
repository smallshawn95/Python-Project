import json, datetime

with open("./CodeForces/codeforces_contest.json", "r", encoding = "utf8") as file:
    codeforces_contest = json.load(file)

for contest in codeforces_contest["result"]:
    if contest["relativeTimeSeconds"] < 0:
        start_time = datetime.datetime.fromtimestamp(contest["startTimeSeconds"])
        print(f"{contest['id']}: {contest['name']} {start_time}")
