import pandas as pd
import pytest

from src.validator import validate_schema


def test_validate_schema_returns_true_for_valid_dataframe():
    df = pd.DataFrame(
        {
            "OCC_HOUR": [8, 17],
            "NEIGHBOURHOOD_158": ["Downtown", "North York"],
            "LONG_WGS84": [-79.38, -79.42],
            "LAT_WGS84": [43.65, 43.75],
        }
    )

    result = validate_schema(df)

    assert result is True


def test_validate_schema_raises_valueerror_when_one_required_column_is_missing():
    df = pd.DataFrame(
        {
            "OCC_HOUR": [8, 17],
            "NEIGHBOURHOOD_158": ["Downtown", "North York"],
            "LONG_WGS84": [-79.38, -79.42],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns: LAT_WGS84"):
        validate_schema(df)


def test_validate_schema_raises_valueerror_when_multiple_required_columns_are_missing():
    df = pd.DataFrame(
        {
            "OCC_HOUR": [8, 17],
            "NEIGHBOURHOOD_158": ["Downtown", "North York"],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns: LONG_WGS84, LAT_WGS84"):
        validate_schema(df)