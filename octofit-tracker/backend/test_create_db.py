from pymongo import MongoClient
from pymongo.errors import PyMongoError

try:
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected to MongoDB successfully.")

    # Initialize the database
    db = client["octofit_db"]
    print("Database initialized: octofit_db")

    # Create collections
    collections = ["users", "teams", "activity", "leaderboard", "workouts"]
    for collection in collections:
        try:
            db.create_collection(collection, capped=False)
            print(f"Collection created: {collection}")
        except PyMongoError as e:
            print(f"Failed to create collection {collection}: {e}")

    print("Database and collections creation process completed.")

except PyMongoError as e:
    print("An error occurred while connecting to MongoDB:", e)
