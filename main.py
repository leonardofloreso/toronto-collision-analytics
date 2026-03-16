from pathlib import Path

import pandas as pd

from src.loader import load_dataset
from src.validator import validate_schema
from src.cleaning import (
    clean_missing_neighbourhood_values,
    remove_invalid_geographic_coordinates,
)

DATA_FILE = Path("data/Traffic_Collisions_Open_Data.csv")


def prepare_dataset(file_path: str | Path) -> pd.DataFrame:
    """
    Load, validate, and clean the Toronto collision dataset.
    Returns a cleaned pandas DataFrame.
    """
    df = load_dataset(str(file_path))
    validate_schema(df)

    df = clean_missing_neighbourhood_values(df)
    df = remove_invalid_geographic_coordinates(df)

    return df


def main() -> None:
    try:
        raw_df = load_dataset(str(DATA_FILE))
        validate_schema(raw_df)

        initial_rows = len(raw_df)
        initial_missing_neighbourhoods = raw_df["NEIGHBOURHOOD_158"].isna().sum()
        initial_invalid_coords = (
            raw_df["LAT_WGS84"].isna()
            | raw_df["LONG_WGS84"].isna()
            | (raw_df["LAT_WGS84"] == 0)
            | (raw_df["LONG_WGS84"] == 0)
            | (~raw_df["LAT_WGS84"].between(-90, 90))
            | (~raw_df["LONG_WGS84"].between(-180, 180))
        ).sum()

        cleaned_df = prepare_dataset(DATA_FILE)

        final_rows = len(cleaned_df)
        final_unknown_neighbourhoods = (
            cleaned_df["NEIGHBOURHOOD_158"].astype(str).str.strip().eq("Unknown").sum()
        )
        final_invalid_coords = (
            cleaned_df["LAT_WGS84"].isna()
            | cleaned_df["LONG_WGS84"].isna()
            | (cleaned_df["LAT_WGS84"] == 0)
            | (cleaned_df["LONG_WGS84"] == 0)
            | (~cleaned_df["LAT_WGS84"].between(-90, 90))
            | (~cleaned_df["LONG_WGS84"].between(-180, 180))
        ).sum()

        print("Dataset loaded, validated, and cleaned successfully.")
        print(f"Rows loaded: {initial_rows}")
        print(f"Rows after cleaning: {final_rows}")
        print(f"Columns loaded: {len(cleaned_df.columns)}")
        print(f"Initial missing neighbourhoods: {initial_missing_neighbourhoods}")
        print(f"Neighbourhoods standardized to 'Unknown': {final_unknown_neighbourhoods}")
        print(f"Invalid coordinate rows before cleaning: {initial_invalid_coords}")
        print(f"Invalid coordinate rows after cleaning: {final_invalid_coords}")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()