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
        db.create_collection(collection, capped=False)
        print(f"Collection created: {collection}")

    # Ensure unique index for users collection
    db.users.create_index("email", unique=True)
    print("Unique index created on 'email' field in users collection.")

    print("Database and collections initialized successfully.")

except PyMongoError as e:
    print("An error occurred:", e)
