from pymongo import MongoClient
import logging
import os

async def db_connection():
    try:
        mongodb_uri = os.getenv("MONGODB_URI")
        client = MongoClient(mongodb_uri)
        db = client.website
        if db is not None:
            logging.info("Database is connected")
            return db
        else:
            logging.error("Database connection error")
            return None
    except Exception as e:
        logging.error("Error connecting to database: %s", e)
        return None
