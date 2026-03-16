from pathlib import Path

import streamlit as st

from main import prepare_dataset

DATA_FILE = Path("data/Traffic_Collisions_Open_Data.csv")


@st.cache_data
def load_clean_data():
    return prepare_dataset(DATA_FILE)


def collisions_by_hour(df):
    hourly = (
        df.groupby("OCC_HOUR")
        .size()
        .reset_index(name="Collision_Count")
        .sort_values("OCC_HOUR")
    )
    return hourly


def top_neighbourhoods(df, top_n=10):
    neighbourhoods = (
        df.groupby("NEIGHBOURHOOD_158")
        .size()
        .reset_index(name="Collision_Count")
        .sort_values("Collision_Count", ascending=False)
        .head(top_n)
    )
    return neighbourhoods


def main():
    st.set_page_config(
        page_title="Toronto Collision Analytics",
        layout="wide"
    )

    st.title("Toronto Traffic Collision Analytics Tool")
    st.write("Sprint 1 - Basic dashboard for cleaned collision data")

    try:
        df = load_clean_data()

        st.subheader("Dataset Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("Rows", f"{len(df):,}")
        col2.metric("Columns", len(df.columns))
        col3.metric("Neighbourhoods", df["NEIGHBOURHOOD_158"].nunique())

        st.subheader("Cleaned Data Preview")
        st.dataframe(df.head(20), use_container_width=True)

        st.subheader("Collisions by Hour")
        hourly_df = collisions_by_hour(df)
        st.bar_chart(hourly_df.set_index("OCC_HOUR"))

        st.subheader("Top 10 Neighbourhoods by Collision Count")
        neighbourhood_df = top_neighbourhoods(df, top_n=10)
        st.bar_chart(neighbourhood_df.set_index("NEIGHBOURHOOD_158"))

    except FileNotFoundError:
        st.error("Dataset file not found. Make sure it exists in the data folder.")
    except ValueError as e:
        st.error(f"Validation error: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()