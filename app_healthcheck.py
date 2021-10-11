import os
import uuid

from flask import Flask, redirect, url_for, jsonify, make_response


class HealthLevel(object):
    DOWN = "down\n"
    UP = "up\n"
    MAINTENANCE = "maint\n"
    READY = "ready\n"


name = os.environ.get("FLASK_APP_NAME", uuid.uuid4())
app = Flask(__name__)


@app.route("/")
def health_check():
    health_level = os.environ.get("FLASK_HEALTH_LEVEL", HealthLevel.READY)
    return health_level


if __name__ == '__main__':
    print("FLASK_APP_NAME: {}".format(name))
    app.run(host="0.0.0.0", port=8080)
