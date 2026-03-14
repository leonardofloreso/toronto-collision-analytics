import pandas as pd
import matplotlib.pyplot as plt


def collisions_by_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group collisions by weekday and return a dataframe with all 7 days
    in the correct order.
    """
    if "OCC_DOW" not in df.columns:
        raise ValueError("Dataset must contain 'OCC_DOW' column.")

    weekday_order = [
    "Monday","Tuesday","Wednesday",
    "Thursday","Friday","Saturday","Sunday"
    ]

    weekday_counts = (
        df["OCC_DOW"]
        .dropna()
        .value_counts()
        .reindex(weekday_order, fill_value=0)
        .reset_index()
    )

    weekday_counts.columns = ["OCC_DOW", "collision_count"]

    return weekday_counts


def plot_collisions_by_weekday(weekday_data: pd.DataFrame):
    """
    Create a bar chart of collision counts by weekday.
    """
    required_columns = {"OCC_DOW", "collision_count"}
    if not required_columns.issubset(weekday_data.columns):
        raise ValueError(
            "weekday_data must contain 'OCC_DOW' and 'collision_count' columns."
        )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(
        weekday_data["OCC_DOW"],
        weekday_data["collision_count"],
        edgecolor="black",
        linewidth=0.8,
    )

    ax.set_title("Traffic Collisions by Weekday", fontsize=16, fontweight="bold", pad=15)
    ax.set_xlabel("Day of Week", fontsize=12)
    ax.set_ylabel("Number of Collisions", fontsize=12)

    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    return fig
