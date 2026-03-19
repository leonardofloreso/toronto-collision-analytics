import streamlit as st
import pandas as pd

from analytics import (
    collisions_by_weekday,
    plot_collisions_by_weekday,
    collisions_by_year,
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
    plot_collisions_by_year,
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

st.subheader("Data Preview")
st.dataframe(df.head(10), use_container_width=True)

# --- Analytics calculations ---

weekday_data = collisions_by_weekday(df)
road_user_data = collisions_by_road_user(df)
hourly_data = collisions_by_hour(df)
neighbourhood_counts = collisions_by_neighbourhood(df)

# Use only full years for yearly trend analysis
df_yearly = df[(df["OCC_YEAR"] >= 2015) & (df["OCC_YEAR"] <= 2024)]
yearly_data = collisions_by_year(df_yearly)

# --- Generate plots ---

weekday_fig = plot_collisions_by_weekday_styled(weekday_data)
hour_fig = plot_collisions_by_hour(hourly_data)
neighbourhood_fig = plot_collisions_by_neighbourhood(neighbourhood_counts)
road_user_fig = plot_road_user_distribution(road_user_data)
yearly_fig = plot_collisions_by_year(yearly_data)

# --- Dashboard layout ---

st.subheader("Collision Analytics Results")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Collisions by Weekday")
    st.pyplot(weekday_fig)

with col2:
    st.markdown("### Collisions by Hour")
    st.pyplot(hour_fig)

st.markdown("### Yearly Collision Trends (2015–2024)")
st.pyplot(yearly_fig)

st.markdown("**Key Insights:**")

st.markdown("""
- Collisions increased steadily between 2015–2019  
- Sharp drop in 2020 (likely COVID-19 impact)  
- Recovery trend observed from 2022 onward  
""")

st.markdown("### Top Collision Neighbourhoods")
st.pyplot(neighbourhood_fig)

st.markdown("### Road User Involvement Distribution")
st.pyplot(road_user_fig)