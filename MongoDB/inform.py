from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

database = client["ShaoJiJi"]
collection = database["inform"]

inform_data = {
    "guild": 1021706869124894720,
    "setting": {
        "birthday": {
            "channel": None,
            "content": {
                "text": "Today is <AD>-<Month>-<Day>！祝 <user> <age>歲生日快樂！",
                "color": "#9B59B6"
            }
        },
        "gasoline": {
            "channel": None
        },
        "typhoon": {
            "channel": None
        },
        "twelve_midnight": {
            "channel": None
        }
    }
}

collection.insert_one(inform_data)
