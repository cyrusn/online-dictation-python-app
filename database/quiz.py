import pymongo
from bson.objectid import ObjectId
from typing import TypedDict, List

from .db import DB


class Vocabulary(TypedDict):
    """represent a vocabulary"""

    quiz_name: str
    title: str
    definition: str
    part_of_speech: str


class Quiz(DB):
    """A quiz contain list of vocabulary"""

    def __init__(self, dbName: str, dsn: str):
        super().__init__(dbName, dsn)
        self.collection_name = "quiz"
        self.quiz_col = super().get_collection(self.collection_name)

        self.quiz_col.create_index(
            [("quiz_name", pymongo.DESCENDING), ("title", pymongo.ASCENDING)],
            unique=True
        )

    def drop_collection(self):
        super().drop_collection(self.collection_name)

    def insert_quiz(self, vocabs: List[Vocabulary]):
        return self.quiz_col.insert_many(vocabs)

    @property
    def quiz_names(self):
        return self.quiz_col.distinct("quiz_name")

    def find_ids_by_quiz_name(self, quiz_name: str) -> List[str]:
        """Find all vocabulary ids by name"""
        ids = self.quiz_col.distinct(
            "_id", {"quiz_name": quiz_name})
        return [str(id) for id in ids]

    def find_vocab_by_id(self, id: str) -> Vocabulary:
        return self.quiz_col.find_one({"_id": ObjectId(id)})


if __name__ == "__main__":
    quiz = Quiz("online_dictation_trial", "mongodb://localhost:27017/")
    print(quiz.quiz_names)
