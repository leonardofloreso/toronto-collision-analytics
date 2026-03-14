import pandas as pd

from src.analysis import collisions_by_hour


def test_collisions_by_hour_returns_hourly_counts():
    df = pd.DataFrame({
        "OCC_HOUR": [8, 8, 9, 10, 10, 10]
    })

    result = collisions_by_hour(df)

    expected = pd.DataFrame({
        "OCC_HOUR": [8, 9, 10],
        "collision_count": [2, 1, 3]
    })

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)