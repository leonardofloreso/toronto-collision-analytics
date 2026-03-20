import streamlit as st
import pandas as pd

from src.analytics import (
    collisions_by_weekday,
    plot_collisions_by_weekday,
    collisions_by_year,
    collisions_by_month,
)

from src.analysis import (
    collisions_by_road_user,
    collisions_by_hour,
    collisions_by_neighbourhood,
)

from src.plots import (
    plot_collisions_by_neighbourhood,
    plot_collisions_by_hour,
    plot_road_user_distribution,
    plot_collisions_by_weekday_styled,
    plot_collisions_by_year,
    plot_collisions_by_month,
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

# --- Filters ---

st.sidebar.header("Filters")

year_options = sorted(df["OCC_YEAR"].dropna().unique().tolist())
selected_years = st.sidebar.multiselect(
    "Select Year(s)",
    options=year_options,
    default=year_options
)

neighbourhood_options = sorted(df["NEIGHBOURHOOD_158"].dropna().unique().tolist())
selected_neighbourhoods = st.sidebar.multiselect(
    "Select Neighbourhood(s)",
    options=neighbourhood_options,
    default=neighbourhood_options
)

filtered_df = df[
    df["OCC_YEAR"].isin(selected_years) &
    df["NEIGHBOURHOOD_158"].isin(selected_neighbourhoods)
]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()


# --- Dataset summary and preview ---

st.subheader("Dataset Summary")

col_a, col_b, col_c = st.columns(3)

col_a.metric("Rows", f"{len(filtered_df):,}")
col_b.metric("Columns", len(filtered_df.columns))
col_c.metric("Neighbourhoods", filtered_df["NEIGHBOURHOOD_158"].nunique())


st.subheader("Data Preview")
st.dataframe(filtered_df.head(10), use_container_width=True)


# --- Analytics calculations ---

weekday_data = collisions_by_weekday(filtered_df)
road_user_data = collisions_by_road_user(filtered_df)
hourly_data = collisions_by_hour(filtered_df)
neighbourhood_counts = collisions_by_neighbourhood(filtered_df)

# Use only full years for yearly trend analysis
df_yearly = filtered_df[(filtered_df["OCC_YEAR"] >= 2015) & (filtered_df["OCC_YEAR"] <= 2024)]
yearly_data = collisions_by_year(df_yearly)

month_data = collisions_by_month(filtered_df)



# --- Generate plots ---

weekday_fig = plot_collisions_by_weekday_styled(weekday_data)
hour_fig = plot_collisions_by_hour(hourly_data)
neighbourhood_fig = plot_collisions_by_neighbourhood(neighbourhood_counts)
road_user_fig = plot_road_user_distribution(road_user_data)
yearly_fig = plot_collisions_by_year(yearly_data)
month_fig = plot_collisions_by_month(month_data)


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

st.markdown("### Monthly Collision Trends")
st.pyplot(month_fig)