from flask import Flask, redirect, url_for, jsonify, make_response
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return "Hello World: {}".format(ip_address)


@app.route("/healthcheck")
def healthcheck():
    return make_response(
        jsonify(
            status="OK",
        ),
        200
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
