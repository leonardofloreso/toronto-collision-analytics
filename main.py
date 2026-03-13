from src.loader import load_dataset
from src.validator import validate_schema
import pandas as pd
from src.cleaning import (
    clean_missing_neighbourhood_values,
    remove_invalid_geographic_coordinates
) 


def main() -> None:
    file_path = "data/Traffic_Collisions_Open_Data.csv"

    df = load_dataset(file_path)
    validate_schema(df)

    print("Dataset loaded and validated successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(df.head())
    
    df=clean_missing_neighbourhood_values(df) 
    df=remove_invalid_geographic_coordinates(df) 
    print("Data cleaning completed.")
    print(f"Rows after cleaning: {df.shape[0]}")


if __name__ == "__main__":
    main()