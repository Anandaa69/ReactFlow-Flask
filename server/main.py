from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/users", methods=["GET"])
def users():
    users = {
        "users": [
            "steve",
            "john",
            "jane",
        ]
    }
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
