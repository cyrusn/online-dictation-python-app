from database.quiz import Quiz
import json
import os


def run(args):
    quiz = Quiz(args.db_name, args.dsn)
    quiz_name = os.path.basename(args.file).split(".")[0]
    print(f"importing quiz: {quiz_name}")

    if args.overwrite:
        print(f"dropping quiz collection")
        quiz.drop_collection()

    if os.path.isfile(args.file):
        with open(args.file, "r", encoding='utf-8-sig') as file:
            quiz_json = json.load(file)
            # add quiz_name to all vocabs
            for vocab in quiz_json:
                vocab["quiz_name"] = quiz_name
            result = quiz.insert_quiz(quiz_json)
            print(
                f"{len(result.inserted_ids)} vocabularies are successfully imported")
            return

    print('invalid file path')


def add_argument(parser, config=None):
    parser.add_argument(
        "file", help='path of quiz json file')
    parser.add_argument("--dsn", '-d', help='dsn of mongodb')
    parser.add_argument("--db_name",  help='dbName of database in mongodb')
    parser.add_argument(
        "--overwrite", action='store_true',
        help='drop the quiz collection and import again')
    parser.set_defaults(
        **{k: v for (k, v) in config.items() if k in ["dsn", "db_name"]}
    )
    parser.set_defaults(func=run)
