"""
Zadanie: test-github-workflow
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    Return a message with a header.
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
