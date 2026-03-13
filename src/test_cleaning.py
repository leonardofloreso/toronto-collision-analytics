from cleaning import (
    clean_missing_neighbourhood_values,
    remove_invalid_geographic_coordinates
)

df = clean_missing_neighbourhood_values(df, column="NEIGHBOURHOOD_158")
df = remove_invalid_geographic_coordinates(df, lat_col="LATITUDE", lon_col="LONGITUDE")