from pymongo.mongo_client import MongoClient

uri = os.getenv("DATABASE_URL")

client = MongoClient(uri)

db = client.item_db

collection = db["item_collection"]

user_collection = db["user_collection"]