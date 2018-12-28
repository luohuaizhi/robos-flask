from flask import Flask
from flask import jsonify


app = Flask("app")


@app.route("/test", methods=["GET"])
def test():
    return jsonify({"msg": "test"})


if __name__ == "__main__":
    app.run()
