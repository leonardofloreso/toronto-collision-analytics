import pandas as pd


def collisions_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    result = (
        df.groupby("OCC_HOUR")
        .size()
        .reset_index(name="collision_count")
        .sort_values("OCC_HOUR")
    )
    return result