import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_prices():
    path = os.path.join(DATA_DIR, "brent_oil_prices.csv")
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()
    return df

def load_events():
    path = os.path.join(DATA_DIR, "oil_market_events.csv")
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()   # handles date/event lowercase
    return df

def load_change_points():
    path = os.path.join(DATA_DIR, "change_points.csv")
    if not os.path.exists(path):
        raise FileNotFoundError("change_points.csv not found")

    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()
    return df
