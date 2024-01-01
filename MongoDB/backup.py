import json
from bson import ObjectId
from pymongo import MongoClient

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient("mongodb://localhost:27017/")

data = {}
database = client["ShaoJiJi"]
for collection_name in database.list_collection_names():
    collection = database[collection_name]
    data[collection_name] = list(collection.find({}))

with open("./MongoDb/backup.json", "w", encoding = "utf8") as file:
    json.dump(data, file, indent = 4, ensure_ascii = False, cls = CustomJSONEncoder)
