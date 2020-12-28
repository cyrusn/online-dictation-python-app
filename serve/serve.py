from flask import Flask, jsonify, send_file, request, abort
from os.path import join, dirname, abspath
from sys import argv

from database.quiz import Quiz


def run(port=5000, static="static", dsn='mongodb://localhost:27017/',
        dbName='online_dictation_trial'):
    static_folder = abspath(join(dirname(argv[0]), static))
    app = Flask(__name__, static_folder=static_folder)
    quiz = Quiz(dbName=dbName, dsn=dsn)

    print(f"Serving static folder: {static_folder}")

    @app.route("/api")
    def hello():
        return jsonify({"message": "hello world"})

    @app.route("/api/quiz")
    def get_quiz_names():
        return jsonify(quiz.quiz_names)

    @app.route("/api/quiz/<quiz_name>")
    def get_ids_by_quiz_name(quiz_name):
        return jsonify(quiz.find_ids_by_quiz_name(quiz_name))

    @app.route("/api/vocab/<id>")
    def get_vocab_by_id(id):
        vocab = quiz.find_vocab_by_id(id)
        vocab['_id'] = str(vocab['_id'])
        return jsonify(vocab)

    @app.route("/")
    def root():
        return app.send_static_file("index.html")

    @app.route("/<path:filename>")
    def static_proxy(filename):
        return app.send_static_file(filename)

    app.run(port=port)


if __name__ == "__main__":
    run()
