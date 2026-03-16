import pandas as pd
import pytest

from src.cleaning import (
    clean_missing_neighbourhood_values,
    remove_invalid_geographic_coordinates,
)


def test_clean_missing_neighbourhood_values_replaces_missing_and_blank():
    df = pd.DataFrame({
        "NEIGHBOURHOOD_158": ["Downtown", None, "", "  ", "N/A", "Scarborough"]
    })

    result = clean_missing_neighbourhood_values(df)

    expected = ["Downtown", "Unknown", "Unknown", "Unknown", "Unknown", "Scarborough"]
    assert result["NEIGHBOURHOOD_158"].tolist() == expected


def test_clean_missing_neighbourhood_values_strips_spaces():
    df = pd.DataFrame({
        "NEIGHBOURHOOD_158": ["  North York  "]
    })

    result = clean_missing_neighbourhood_values(df)

    assert result["NEIGHBOURHOOD_158"].iloc[0] == "North York"


def test_clean_missing_neighbourhood_values_raises_error_if_column_missing():
    df = pd.DataFrame({"OTHER_COLUMN": ["A", "B"]})

    with pytest.raises(ValueError, match="not found"):
        clean_missing_neighbourhood_values(df)


def test_remove_invalid_geographic_coordinates_removes_bad_rows():
    df = pd.DataFrame({
        "LAT_WGS84": [43.7, 0, None, 95, 43.65],
        "LONG_WGS84": [-79.4, -79.3, -79.2, -79.1, 0]
    })

    result = remove_invalid_geographic_coordinates(df)

    assert len(result) == 1
    assert result.iloc[0]["LAT_WGS84"] == 43.7
    assert result.iloc[0]["LONG_WGS84"] == -79.4


def test_remove_invalid_geographic_coordinates_raises_error_if_column_missing():
    df = pd.DataFrame({
        "LAT": [43.7],
        "LON": [-79.4]
    })

    with pytest.raises(ValueError, match="not found"):
        remove_invalid_geographic_coordinates(df)