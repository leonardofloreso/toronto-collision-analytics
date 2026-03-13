import matplotlib.pyplot as plt
import pandas as pd


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