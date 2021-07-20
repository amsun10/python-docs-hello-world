from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return redirect("http://localhost:5000/flag", code=302)


if __name__ == '__main__':
    app.run()
