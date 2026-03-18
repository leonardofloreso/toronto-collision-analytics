import pandas as pd


INVALID_NEIGHBOURHOOD_VALUES = {"NSA", "UNKNOWN"}


def collisions_by_neighbourhood(df: pd.DataFrame) -> dict:
    """
    Count collisions by neighbourhood.

    Uses 'NEIGHBOURHOOD' if present; otherwise falls back to
    'NEIGHBOURHOOD_158'. Excludes invalid values such as NSA and UNKNOWN.
    """
    column = _get_neighbourhood_column(df)

    cleaned_series = df[column].astype(str).str.strip()
    filtered_series = cleaned_series[
        ~cleaned_series.str.upper().isin(INVALID_NEIGHBOURHOOD_VALUES)
    ]

    return filtered_series.value_counts().to_dict()


def collisions_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count collisions by hour and return results sorted by OCC_HOUR.
    """
    return (
        df.groupby("OCC_HOUR")
        .size()
        .reset_index(name="collision_count")
        .sort_values("OCC_HOUR")
    )


def _get_neighbourhood_column(df: pd.DataFrame) -> str:
    """
    Return the appropriate neighbourhood column name from the dataframe.
    """
    if "NEIGHBOURHOOD" in df.columns:
        return "NEIGHBOURHOOD"
    if "NEIGHBOURHOOD_158" in df.columns:
        return "NEIGHBOURHOOD_158"
    raise KeyError("No neighbourhood column found in dataframe")


def collisions_by_road_user(df: pd.DataFrame) -> dict:
    road_user_columns = ["AUTOMOBILE", "MOTORCYCLE", "PASSENGER", "BICYCLE", "PEDESTRIAN"]

    result = {}

    for col in road_user_columns:
        cleaned = df[col].astype(str).str.strip().str.upper()
        result[col] = (cleaned == "YES").sum()

    return result