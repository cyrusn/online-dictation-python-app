import bcrypt
import pymongo
from enum import IntEnum
from bson.objectid import ObjectId
from typing import TypedDict, List

from .db import DB


class Role(IntEnum):
    TEACHER = 0
    STUDENT = 1


class User(TypedDict):
    """Represents an user."""

    userAlias: str
    password: str
    role: Role


class DBUser(TypedDict):
    """Represents an user but with hashed password."""

    _id: ObjectId
    userAlias: str
    password: bytes
    role: Role


class Auth(DB):
    def __init__(self, dbName: str, dsn: str):
        self.dbName = dbName
        self.collection_name = "auth"
        super().__init__(dbName, dsn)

        self.auth_col = super().get_collection(self.collection_name)
        self.auth_col.create_index(
            [("userAlias", pymongo.ASCENDING)], unique=True)

    def drop_collection(self):
        super().drop_collection(self.collection_name)

    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt(12)
        bpassword = bytes(password, "utf-8")
        hashed = bcrypt.hashpw(bpassword, salt)
        return hashed

    def insert_users(self, users: List[User]):
        class hashedPasswordUser(TypedDict):
            userAlias: str
            password: bytes  # hashed password is formated as bytes
            role: Role

        def hashUserPW(u: User) -> hashedPasswordUser:
            user: hashedPasswordUser = {
                "userAlias": u["userAlias"],
                "password": self.hash_password(u["password"]),
                "role": u["role"],
            }
            return user

        hashedUsers: List[hashedPasswordUser] = list(map(hashUserPW, users))
        return self.auth_col.insert_many(hashedUsers)

    def find_user(self, userAlias: str):
        return self.auth_col.find_one({"userAlias": userAlias})

    def authorize(self, u: User) -> bool:
        userAlias = u["userAlias"]
        password = u["password"]
        user: DBUser = self.find_user(userAlias)
        return bcrypt.checkpw(bytes(password, "utf-8"), user["password"])
