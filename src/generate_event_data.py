import os
import sys
import pandas as pd
from typing import List, Tuple


EVENTS: List[Tuple[str, str]] = [
    ("1990-08-02", "Iraq invades Kuwait"),
    ("1997-07-02", "Asian Financial Crisis"),
    ("2001-09-11", "September 11 terrorist attacks"),
    ("2003-03-20", "US-led invasion of Iraq"),
    ("2008-09-15", "Global Financial Crisis"),
    ("2011-02-15", "Arab Spring uprisings"),
    ("2014-11-27", "OPEC decision to maintain production"),
    ("2016-11-30", "OPEC production cut agreement"),
    ("2018-05-08", "US withdraws from Iran nuclear deal"),
    ("2019-09-14", "Attack on Saudi Aramco facilities"),
    ("2020-03-11", "COVID-19 declared a pandemic"),
    ("2020-04-20", "Historic oil price collapse"),
    ("2021-10-01", "Global energy supply crunch"),
    ("2022-02-24", "Russia invades Ukraine"),
    ("2022-06-01", "EU sanctions on Russian oil"),
]


def build_events_df(events: List[Tuple[str, str]]) -> pd.DataFrame:
    """
    Build a DataFrame containing oil market events.

    Parameters
    ----------
    events : list of tuples
        Each tuple contains (event_date, event_description)

    Returns
    -------
    pd.DataFrame
        Structured DataFrame with parsed dates
    """
    df = pd.DataFrame(events, columns=["date", "event"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if df["date"].isna().any():
        raise ValueError("One or more event dates could not be parsed.")

    return df.sort_values("date").reset_index(drop=True)


def save_events(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the events DataFrame to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Events DataFrame
    output_path : str
        Destination CSV path
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
    except OSError as exc:
        raise RuntimeError(f"Failed to write events file: {exc}") from exc


def main() -> None:
    """
    Main execution function.
    """
    output_file = os.path.join("data", "events", "oil_market_events.csv")

    try:
        events_df = build_events_df(EVENTS)
        save_events(events_df, output_file)
        print(f"✔ Events file successfully created at: {output_file}")
    except Exception as exc:
        print(f"✖ Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
