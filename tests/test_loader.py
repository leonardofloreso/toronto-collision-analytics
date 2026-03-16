import pandas as pd
import pytest

from src.loader import load_dataset


def test_load_dataset_returns_dataframe_for_valid_csv(tmp_path):
    file_path = tmp_path / "sample.csv"
    df = pd.DataFrame(
        {
            "OCC_HOUR": [8, 17],
            "NEIGHBOURHOOD_158": ["Downtown", "North York"],
            "LONG_WGS84": [-79.38, -79.42],
            "LAT_WGS84": [43.65, 43.75],
        }
    )
    df.to_csv(file_path, index=False)

    result = load_dataset(str(file_path))

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert list(result.columns) == list(df.columns)


def test_load_dataset_raises_filenotfound_for_missing_file():
    with pytest.raises(FileNotFoundError, match="Dataset file not found"):
        load_dataset("data/this_file_does_not_exist.csv")


def test_load_dataset_raises_valueerror_for_empty_csv(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    with pytest.raises(ValueError, match="Dataset file is empty"):
        load_dataset(str(file_path))


def test_load_dataset_raises_valueerror_for_csv_with_headers_but_no_rows(tmp_path):
    file_path = tmp_path / "headers_only.csv"
    file_path.write_text("OCC_HOUR,NEIGHBOURHOOD_158,LONG_WGS84,LAT_WGS84\n")

    with pytest.raises(ValueError, match="Dataset loaded but contains no rows"):
        load_dataset(str(file_path))