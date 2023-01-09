from flask import jsonify, Blueprint, request
from flask import current_app as app
from tasks import heavy_math_task

bp = Blueprint("blueprint", __name__)


def handle_exception(error):
    app.logger.error(f"Error in routes: {error}", exc_info=True)
    return jsonify({"success": False, "data": None})


@bp.route("/status", methods=["GET"])
def status():
    return jsonify({"success": True, "data": "It works"})


@bp.route("/new", methods=["POST"])
def new_task():
    body = request.get_json()
    val = body.get("val", 1)

    app.logger.info(f"Starting task val = {val}")
    heavy_math_task.delay(val)
    app.logger.info(f"Started task val = {val}")

    return jsonify({"success": True, "data": None})
