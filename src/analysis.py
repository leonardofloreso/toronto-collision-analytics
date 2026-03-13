import pandas as pd


def collisions_by_neighbourhood(df: pd.DataFrame) -> dict:
    result = (
        df["NEIGHBOURHOOD"]
        .value_counts()
        .to_dict()
    )
    return result