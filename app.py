import os
import uuid

from flask import Flask, redirect, url_for, jsonify, make_response

name = os.environ.get("FLASK_APP_NAME", uuid.uuid4())
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World: {}".format(name)


@app.route("/healthcheck")
def healthcheck():
    return make_response(
        jsonify(
            status="OK",
        ),
        200
    )


if __name__ == '__main__':
    print("FLASK_APP_NAME: {}".format(name))
    app.run(host="0.0.0.0", port=5000)
