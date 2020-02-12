import pymongo


class DB:
    def __init__(self, dbName: str, dsn: str):
        client = pymongo.MongoClient(dsn)
        self.client = client[dbName]

    def get_collection(self, collection_name: str) -> pymongo.collection:
        return self.client[collection_name]

    def drop_collection(self, collection_name: str):
        self.client.drop_collection(collection_name)
