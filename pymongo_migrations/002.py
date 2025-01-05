"""
Migration script for adding TTL index on 'date_created' field to users collection
"""
import pymongo.database
import pymongo.errors

name = '002'
dependencies = ['001']


def upgrade(db: pymongo.database.Database):
    try:
        db.test_users.create_index(
            [("date_created", 1)],
            partialFilterExpression={"is_tmp": {"$eq": True}},
            expireAfterSeconds=24 * 60 * 60,
            name="i_delete_tmp_users"
        )
    except pymongo.errors.OperationFailure as e:
        if e.code == 85:
            print("Index already exists, skipping creation")
        else:
            raise e


def downgrade(db: pymongo.database.Database):
    try:
        db.test_users.drop_index("i_delete_tmp_users")
    except pymongo.errors.OperationFailure as e:
        if e.code == 27:
            print("Index doesn't exist, skipping deletion")
        else:
            raise e
