from flask import Flask, jsonify

app = Flask(__name__)


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
