
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Agile DevOps Assignment 2</h1>
    <h2>Flask Application Running Successfully!</h2>
    <p>Technologies: Python, Flask, Docker, GitHub Actions</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
