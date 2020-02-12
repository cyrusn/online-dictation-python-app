from unittest import TestCase, main
from auth import Auth, User, Role
from typing import List

auth = Auth("online_dictation", "mongodb://localhost:27017/")

users: List[User] = [
    {"userAlias": "lpcyn", "password": "abc123", "role": Role.TEACHER},
    {"userAlias": "lpthn", "password": "abc123", "role": Role.TEACHER},
    {"userAlias": "lpcyl", "password": "abc123", "role": Role.TEACHER},
    {"userAlias": "lp000001", "password": "abc123", "role": Role.STUDENT},
    {"userAlias": "lp000002", "password": "abc123", "role": Role.STUDENT},
]


class TestAuth(TestCase):
    def test_insert_users(self):
        auth.drop_collection()
        indexes = auth.insert_users(users)
        self.assertEqual(len(indexes.inserted_ids), 5)

    def test_auth(self):
        users = [
            ({"userAlias": "lpcyn", "password": "abc123", "role": Role.TEACHER}, True),
            ({"userAlias": "lpthn", "password": "abc132", "role": Role.TEACHER}, False),
        ]

        for u in users:
            self.assertEqual(auth.authorize(u[0]), u[1])


if __name__ == "__main__":
    main()
