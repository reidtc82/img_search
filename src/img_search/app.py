from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Print 'Hellow World!' as the response body."""
    return "Hello World!"


if __name__ == "__main__":
    app.run()
