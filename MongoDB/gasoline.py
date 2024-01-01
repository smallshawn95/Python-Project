import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

database = client["ShaoJiJi"]
collection = database["widget"]

with open("./MongoDB/gasoline.json", "r", encoding = "utf8") as file:
    gasoline = {
        "title": "gasoline",
        "content": json.load(file),
    }

collection.update_one({"title": "gasoline"}, {"$set": gasoline}, upsert = True)

gasoline_data = collection.find_one({"title": "gasoline"})
print(type(gasoline_data))
print(gasoline_data)
