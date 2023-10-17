import json, requests

# https://codeforces.com/apiHelp

# Contests
response = requests.get("https://codeforces.com/api/contest.list")

with open("./CodeForces/codeforces_contest.json", "w", encoding = "utf8") as file:
    json.dump(response.json(), file, indent = 4)

# Gyms
response = requests.get("https://codeforces.com/api/contest.list?gym=true")

with open("./CodeForces/codeforces_gym.json", "w", encoding = "utf8") as file:
    json.dump(response.json(), file, indent = 4)

# Problems
response = requests.get("https://codeforces.com/api/problemset.problems")

with open("./CodeForces/codeforces_problem.json", "w", encoding = "utf8") as file:
    json.dump(response.json(), file, indent = 4)
