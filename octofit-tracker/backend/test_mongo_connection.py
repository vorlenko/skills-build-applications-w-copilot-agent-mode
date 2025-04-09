from pymongo import MongoClient

try:
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    # List databases
    databases = client.list_database_names()
    print("Connection successful. Databases:", databases)
except Exception as e:
    print("Connection failed:", e)
