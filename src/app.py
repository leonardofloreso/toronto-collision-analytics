import streamlit as st
import pandas as pd

from analytics import (
    collisions_by_weekday,
    plot_collisions_by_weekday,
)

from plots import (
    plot_collisions_by_neighbourhood,
    plot_collisions_by_hour
)

DATA_PATH = "Traffic_Collisions_Open_Data.csv"



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

# --- Analytics calculations ---

weekday_data = collisions_by_weekday(df)

# Hourly aggregation (if not already done elsewhere)
hourly_data = (
    df.groupby("OCC_HOUR")
    .size()
    .reset_index(name="collision_count")
)

# Neighbourhood aggregation
neighbourhood_counts = (
    df["NEIGHBOURHOOD_158"]
    .value_counts()
    .to_dict()
)

# --- Generate plots ---

weekday_fig = plot_collisions_by_weekday(weekday_data)
hour_fig = plot_collisions_by_hour(hourly_data)
neighbourhood_fig = plot_collisions_by_neighbourhood(neighbourhood_counts)

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