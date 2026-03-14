import matplotlib.pyplot as plt
import pandas as pd


def plot_collisions_by_neighbourhood(neighbourhood_counts: dict):
    """
    Create a horizontal bar chart of the top 10 neighbourhoods
    with the highest number of collisions.
    """

    # Sort neighbourhoods by collision count (descending)
    sorted_items = sorted(
        neighbourhood_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    names = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))

    ax.barh(names, counts, edgecolor="black")

    ax.invert_yaxis()

    # Titles and labels
    ax.set_title(
        "Top 10 Neighbourhoods by Collision Count",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Number of Collisions")
    ax.set_ylabel("Neighbourhood")

    # Grid for readability
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    return fig


def plot_collisions_by_hour(hourly_data: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(
        hourly_data["OCC_HOUR"],
        hourly_data["collision_count"],
        width=0.8,
        edgecolor="black",
        linewidth=0.6,
    )

    ax.set_title("Hourly Traffic Collisions", fontsize=16, fontweight="bold", pad=15)
    ax.set_xlabel("Hour of Day", fontsize=12)
    ax.set_ylabel("Number of Collisions", fontsize=12)

    ax.set_xticks(range(24))
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    return fig