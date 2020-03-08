from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from time import sleep


def wait_until_connected(dsn):
    connected = False
    while not connected:
        print(f'waiting for database connection: {dsn}')
        try:
            client = MongoClient(dsn, serverSelectionTimeoutMS=2000)
            info = client.server_info()
            connected = True
            print(f"mongodb version: {info['version']}")
        except:
            sleep(2)
