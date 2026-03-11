import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load the Toronto collision dataset from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty.
        RuntimeError: If the file cannot be read as CSV.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Dataset file not found: {file_path}") from exc
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"Dataset file is empty: {file_path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Failed to load dataset: {exc}") from exc

    if df.empty:
        raise ValueError(f"Dataset loaded but contains no rows: {file_path}")

    return df