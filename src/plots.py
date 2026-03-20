import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


PRIMARY_COLOR = "#1f4e79"
SECONDARY_COLOR = "#2a9d8f"
GRID_COLOR = "#d9d9d9"
TEXT_COLOR = "#333333"

def plot_collisions_by_neighbourhood(neighbourhood_counts: dict):
    """
    Create a horizontal bar chart of the top 10 neighbourhoods
    with the highest number of collisions.
    """

    sorted_items = sorted(
        neighbourhood_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    names = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.barh(
        names,
        counts,
        color=PRIMARY_COLOR,
        edgecolor="black",
        linewidth=0.8
    )

    ax.invert_yaxis()

    for i, value in enumerate(counts):
        ax.text(value * 0.99, i, f"{value:,}", va="center", ha="right", color="white", fontsize=9)

    ax.set_title(
        "Top 10 Neighbourhoods by Collision Count",
        fontsize=13,
        fontweight="bold",
        color=TEXT_COLOR,
        pad=12
    )
    ax.set_xlabel("Number of Collisions", fontsize=11, color=TEXT_COLOR)
    ax.set_ylabel("Neighbourhood", fontsize=11, color=TEXT_COLOR)

    ax.grid(axis="x", linestyle="--", alpha=0.5, color=GRID_COLOR)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", colors=TEXT_COLOR, labelsize=9)
    ax.tick_params(axis="y", colors=TEXT_COLOR, labelsize=9)

    plt.tight_layout()
    return fig


def plot_collisions_by_hour(hourly_data: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(
        hourly_data["OCC_HOUR"],
        hourly_data["collision_count"],
        width=0.8,
        color=PRIMARY_COLOR,
        edgecolor="black",
        linewidth=0.8,
    )

    ax.set_title(
        "Hourly Traffic Collisions",
        fontsize=13,
        fontweight="bold",
        color=TEXT_COLOR,
        pad=12
    )
    ax.set_xlabel("Hour of Day", fontsize=11, color=TEXT_COLOR)
    ax.set_ylabel("Number of Collisions", fontsize=11, color=TEXT_COLOR)

    ax.set_xticks(range(24))
    ax.grid(axis="y", linestyle="--", alpha=0.5, color=GRID_COLOR)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", colors=TEXT_COLOR, labelsize=9)
    ax.tick_params(axis="y", colors=TEXT_COLOR, labelsize=9)

    plt.tight_layout()
    return fig


def plot_road_user_distribution(data: dict):
    sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_items]
    values = [item[1] for item in sorted_items]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.barh(
        labels,
        values,
        color=PRIMARY_COLOR,
        edgecolor="black",
        linewidth=0.8
    )

    ax.invert_yaxis()

    for i, value in enumerate(values):
        ax.text(
            value + max(values) * 0.01,
            i,
            f"{value:,}",
            va="center",
            ha="left",
            color=TEXT_COLOR,
            fontsize=9
        )

    ax.set_title(
        "Road User Involvement Distribution",
        fontsize=13,
        fontweight="bold",
        color=TEXT_COLOR,
        pad=12
    )
    ax.set_xlabel("Involvement Count", fontsize=11, color=TEXT_COLOR)
    ax.set_ylabel("Road User Type", fontsize=11, color=TEXT_COLOR)

    ax.grid(axis="x", linestyle="--", alpha=0.5, color=GRID_COLOR)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", colors=TEXT_COLOR, labelsize=9)
    ax.tick_params(axis="y", colors=TEXT_COLOR, labelsize=9)

    plt.tight_layout()
    return fig


def plot_collisions_by_weekday_styled(weekday_data: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(
        weekday_data["OCC_DOW"],
        weekday_data["collision_count"],
        color=PRIMARY_COLOR,
        edgecolor="black",
        linewidth=0.8,
    )

    ax.set_title(
        "Traffic Collisions by Weekday",
        fontsize=13,
        fontweight="bold",
        color=TEXT_COLOR,
        pad=12
    )
    ax.set_xlabel("Day of Week", fontsize=11, color=TEXT_COLOR)
    ax.set_ylabel("Number of Collisions", fontsize=11, color=TEXT_COLOR)

    ax.grid(axis="y", linestyle="--", alpha=0.5, color=GRID_COLOR)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", colors=TEXT_COLOR, labelsize=9)
    ax.tick_params(axis="y", colors=TEXT_COLOR, labelsize=9)

    plt.tight_layout()
    return fig


def plot_collisions_by_year(yearly_data: pd.DataFrame):
    """
    Create a line chart showing collision trends over years.
    """
    required_columns = {"OCC_YEAR", "collision_count"}
    if not required_columns.issubset(yearly_data.columns):
        raise ValueError(
            "yearly_data must contain 'OCC_YEAR' and 'collision_count' columns."
        )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        yearly_data["OCC_YEAR"],
        yearly_data["collision_count"],
        marker="o",
        linewidth=2
    )

    ax.set_title(
        "Yearly Traffic Collision Trends",
        fontsize=16,
        fontweight="bold",
        pad=15,
    )
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Number of Collisions", fontsize=12)

    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    return fig

import matplotlib.pyplot as plt
import pandas as pd


def plot_collisions_by_month(month_data: pd.DataFrame):
    required_columns = {"OCC_MONTH", "collision_count"}
    if not required_columns.issubset(month_data.columns):
        raise ValueError(
            "month_data must contain 'OCC_MONTH' and 'collision_count' columns."
        )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(
        month_data["OCC_MONTH"],
        month_data["collision_count"],
        edgecolor="black",
        linewidth=0.8,
    )

    ax.set_title("Traffic Collisions by Month", fontsize=16, fontweight="bold", pad=15)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Number of Collisions", fontsize=12)

    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig
