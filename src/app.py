import streamlit as st
import pandas as pd

from analytics import (
    collisions_by_weekday,
    plot_collisions_by_weekday,
)

from analysis import (
    collisions_by_road_user,
    collisions_by_hour,
    collisions_by_neighbourhood,
)

from plots import (
    plot_collisions_by_neighbourhood,
    plot_collisions_by_hour,
    plot_road_user_distribution,
    plot_collisions_by_weekday_styled,
)

DATA_PATH = "data/Traffic_Collisions_Open_Data.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


st.set_page_config(
    page_title="Toronto Collision Analytics Dashboard",
    layout="wide"
)

st.title("Toronto Traffic Collision Analytics Dashboard")
st.write(
    "A simple dashboard that displays multiple traffic collision analytics "
    "results and visualizations."
)

# Load dataset
df = load_data()

# --- Dataset summary and preview ---

st.subheader("Dataset Summary")

col_a, col_b, col_c = st.columns(3)

col_a.metric("Rows", f"{len(df):,}")
col_b.metric("Columns", len(df.columns))
col_c.metric("Neighbourhoods", df["NEIGHBOURHOOD_158"].nunique())

st.subheader("Cleaned Data Preview")
st.dataframe(df.head(10), use_container_width=True)

# --- Analytics calculations ---

weekday_data = collisions_by_weekday(df)
road_user_data = collisions_by_road_user(df)
hourly_data = collisions_by_hour(df)
neighbourhood_counts = collisions_by_neighbourhood(df)

# --- Generate plots ---

weekday_fig = plot_collisions_by_weekday_styled(weekday_data)
hour_fig = plot_collisions_by_hour(hourly_data)
neighbourhood_fig = plot_collisions_by_neighbourhood(neighbourhood_counts)
road_user_fig = plot_road_user_distribution(road_user_data)

# --- Dashboard layout ---

st.subheader("Collision Analytics Results")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Collisions by Weekday")
    st.pyplot(weekday_fig)

with col2:
    st.markdown("### Collisions by Hour")
    st.pyplot(hour_fig)

st.markdown("### Top Collision Neighbourhoods")
st.pyplot(neighbourhood_fig)

st.markdown("### Road User Involvement Distribution")
st.pyplot(road_user_fig)