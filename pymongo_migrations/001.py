"""
Migration script for converting date_created field in users collection from int to date type
"""
import datetime
import pymongo.database

name = '001'
dependencies = []


def upgrade(db: "pymongo.database.Database"):
    bulk_operations = [
        pymongo.UpdateOne(
            {"_id": document["_id"]},
            {"$set": {"date_created": datetime.datetime.fromtimestamp(document["date_created"], datetime.UTC)}}
        )
        for document in db.test_users.find({"date_created": {"$type": "int"}})
    ]
    if bulk_operations:
        db.test_users.bulk_write(bulk_operations)


def downgrade(db: "pymongo.database.Database"):
    bulk_operations = [
        pymongo.UpdateOne(
            {"_id": document["_id"]},
            {"$set": {"date_created": int(document["date_created"].timestamp())}}
        )
        for document in db.test_users.find({"date_created": {"$type": "date"}})
    ]
    if bulk_operations:
        db.test_users.bulk_write(bulk_operations)
