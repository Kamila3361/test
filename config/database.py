from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://tasimovakamila:EGD0ds2vVQoiDLdZ@cluster0.o3tzhxt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client.item_db

collection = db["item_collection"]

user_collection = db["user_collection"]