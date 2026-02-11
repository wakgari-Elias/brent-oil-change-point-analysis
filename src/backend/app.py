from flask import Flask
from routes import prices, changepoints, events
from flask import Flask
from flask_cors import CORS

# app = Flask(__name__)
app = Flask(__name__)
CORS(app)  # This allows requests from your React app

# Register Blueprints
app.register_blueprint(prices.bp)
app.register_blueprint(changepoints.bp)
app.register_blueprint(events.bp)

if __name__ == "__main__":
    app.run(debug=True)

