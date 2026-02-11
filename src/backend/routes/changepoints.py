from flask import Blueprint, jsonify
import pandas as pd
import os

bp = Blueprint("changepoints", __name__, url_prefix="/api/changepoints")

@bp.route("/", methods=["GET"])
def get_changepoints():
    try:
        path = "../../data/events/change_points.csv"
        if not os.path.exists(path):
            return jsonify({"error": "change_points.csv not found"})
        df = pd.read_csv(path)
        data = df.to_dict(orient="records")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
