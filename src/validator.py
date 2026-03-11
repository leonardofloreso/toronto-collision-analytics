import pandas as pd


REQUIRED_COLUMNS = [
    "OCC_HOUR",
    "NEIGHBOURHOOD_158",
    "LONG_WGS84",
    "LAT_WGS84",
]


def validate_schema(df: pd.DataFrame) -> bool:
    """
    Validate that the required columns exist in the dataset.

    Args:
        df: Loaded dataset.

    Returns:
        bool: True if schema is valid.

    Raises:
        ValueError: If one or more required columns are missing.
    """
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    return True