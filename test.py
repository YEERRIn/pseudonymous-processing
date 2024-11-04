from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["HEROS"]
collection = db["peopel_data"]


def read_data():
    
    documents = collection.find({})
    for document in documents:
        print(document)


if __name__ == "__main__":
    read_data()
