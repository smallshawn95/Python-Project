import json, requests

# https://codeforces.com/apiHelp

# Contests
response = requests.get("https://codeforces.com/api/contest.list")

with open("./API/CodeForces/contest.json", "w", encoding = "utf8") as file:
    json.dump(response.json(), file, indent = 4)

# Gyms
response = requests.get("https://codeforces.com/api/contest.list?gym=true")

with open("./API/CodeForces/gym.json", "w", encoding = "utf8") as file:
    json.dump(response.json(), file, indent = 4)

# Problems
response = requests.get("https://codeforces.com/api/problemset.problems")

with open("./API/CodeForces/problem.json", "w", encoding = "utf8") as file:
    json.dump(response.json(), file, indent = 4)
