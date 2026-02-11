from flask import Blueprint, jsonify
import pandas as pd

bp = Blueprint("prices", __name__, url_prefix="/api/prices")

@bp.route("/", methods=["GET"])
def get_prices():
    try:
        df = pd.read_csv("../../data/raw/BrentOilPrices.csv")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        data = df.to_dict(orient="records")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
