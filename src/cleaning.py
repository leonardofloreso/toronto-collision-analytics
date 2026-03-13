import pandas as pd


def clean_missing_neighbourhood_values(df: pd.DataFrame, column: str = "NEIGHBOURHOOD_158") -> pd.DataFrame:
    """
    Standardizes missing or inconsistent neighbourhood values.

    Replaces:
    - NaN / None
    - empty strings
    - common placeholder values such as 'Unknown', 'N/A', 'NULL'
    with the value 'Unknown'.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    column : str
        Name of the neighbourhood column.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataframe.")

    cleaned_df = df.copy()

    placeholders = {"", " ", "UNKNOWN", "N/A", "NA", "NULL", "NONE"}

    cleaned_df[column] = cleaned_df[column].apply(
        lambda x: "Unknown"
        if pd.isna(x) or str(x).strip().upper() in placeholders
        else str(x).strip()
    )

    return cleaned_df


def remove_invalid_geographic_coordinates(
    df: pd.DataFrame,
    lat_col: str = "LAT_WGS84",
    lon_col: str = "LONG_WGS84"
) -> pd.DataFrame:
    """
    Removes rows with invalid geographic coordinates.

    Invalid rows include:
    - missing latitude or longitude
    - latitude == 0
    - longitude == 0
    - latitude outside [-90, 90]
    - longitude outside [-180, 180]

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    lat_col : str
        Latitude column name.
    lon_col : str
        Longitude column name.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe with only valid coordinates.
    """
    if lat_col not in df.columns:
        raise ValueError(f"Column '{lat_col}' not found in dataframe.")
    if lon_col not in df.columns:
        raise ValueError(f"Column '{lon_col}' not found in dataframe.")

    cleaned_df = df.copy()

    cleaned_df = cleaned_df.dropna(subset=[lat_col, lon_col])

    cleaned_df = cleaned_df[
        (cleaned_df[lat_col] != 0) &
        (cleaned_df[lon_col] != 0) &
        (cleaned_df[lat_col].between(-90, 90)) &
        (cleaned_df[lon_col].between(-180, 180))
    ]

    return cleaned_df