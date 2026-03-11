from src.loader import load_dataset
from src.validator import validate_schema


def main() -> None:
    file_path = "data/Traffic_Collisions_Open_Data.csv"

    df = load_dataset(file_path)
    validate_schema(df)

    print("Dataset loaded and validated successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(df.head())


if __name__ == "__main__":
    main()