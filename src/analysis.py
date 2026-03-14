import pandas as pd


def collisions_by_neighbourhood(df: pd.DataFrame) -> dict:
    if "NEIGHBOURHOOD" in df.columns:
        column = "NEIGHBOURHOOD"
    elif "NEIGHBOURHOOD_158" in df.columns:
        column = "NEIGHBOURHOOD_158"
    else:
        raise KeyError("No neighbourhood column found in dataframe")

    cleaned_series = df[column].astype(str).str.strip()

    filtered_series = cleaned_series[
        ~cleaned_series.str.upper().isin(["NSA", "UNKNOWN"])
    ]

    result = (
        filtered_series
        .value_counts()
        .to_dict()
    )
    return result

def collisions_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    result = (
        df.groupby("OCC_HOUR")
        .size()
        .reset_index(name="collision_count")
        .sort_values("OCC_HOUR")
    )
    return result