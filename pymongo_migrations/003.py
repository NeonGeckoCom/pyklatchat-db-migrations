"""
Migration script for adding index on 'created_on' field to chats collection
"""
import pymongo.database
import pymongo.errors

name = '003'
dependencies = []


def upgrade(db: pymongo.database.Database):
    try:
        db.chats.create_index(
            [("created_on", -1)],
            unique=False,
            sparse=True,
            name="chat_creation_desc_index"
        )
    except pymongo.errors.OperationFailure as e:
        if e.code == 85:
            print("Index already exists, skipping creation")
        else:
            raise e


def downgrade(db: pymongo.database.Database):
    try:
        db.chats.drop_index("chat_creation_desc_index")
    except pymongo.errors.OperationFailure as e:
        if e.code == 27:
            print("Index doesn't exist, skipping deletion")
        else:
            raise e
