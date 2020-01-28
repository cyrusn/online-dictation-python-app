from flask import Flask, jsonify
from os.path import join, dirname
from sys import argv


def run(port=5000, static="static"):
    static_folder = join(dirname(argv[0]), static)
    app = Flask(__name__, static_folder=static_folder)

    @app.route("/")
    def hello():
        return jsonify({"message": "hello world"})

    @app.route("/static")
    def root():
        # return app.send_static_file("index.html")
        return app.send_static_file("index.html")

    @app.route("/static/<path:filename>")
    def static_proxy(filename):
        # send_static_file will guess the correct MIME type
        return app.send_static_file(filename)

    app.run(port=port)


if __name__ == "__main__":
    run()
