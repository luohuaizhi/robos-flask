from flask import Blueprint
from flask import jsonify

__all__ = ["test_bp"]

test_bp = Blueprint("test", __name__)


@test_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"msg": "test"})
