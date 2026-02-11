from flask import Blueprint, jsonify
import pandas as pd

bp = Blueprint("events", __name__, url_prefix="/api/events")

@bp.route("/", methods=["GET"])
def get_events():
    try:
        df = pd.read_csv("../../data/events/oil_market_events.csv")
        df.rename(columns={"date": "Date", "event": "Event"}, inplace=True)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        data = df.to_dict(orient="records")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
