import pandas as pd
import pytest

from src.analysis import collisions_by_hour, collisions_by_neighbourhood


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


def test_collisions_by_hour_returns_sorted_hours():
    df = pd.DataFrame({
        "OCC_HOUR": [17, 8, 17, 5, 8]
    })

    result = collisions_by_hour(df)

    expected = pd.DataFrame({
        "OCC_HOUR": [5, 8, 17],
        "collision_count": [1, 2, 2]
    })

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)


def test_collisions_by_neighbourhood_returns_counts_using_neighbourhood_158():
    df = pd.DataFrame({
        "NEIGHBOURHOOD_158": [
            "Downtown",
            "Downtown",
            "Scarborough",
            "North York",
            "North York",
            "North York"
        ]
    })

    result = collisions_by_neighbourhood(df)

    expected = {
        "North York": 3,
        "Downtown": 2,
        "Scarborough": 1
    }

    assert result == expected


def test_collisions_by_neighbourhood_uses_neighbourhood_if_present():
    df = pd.DataFrame({
        "NEIGHBOURHOOD": ["Etobicoke", "Etobicoke", "York"],
        "NEIGHBOURHOOD_158": ["Wrong A", "Wrong B", "Wrong C"]
    })

    result = collisions_by_neighbourhood(df)

    expected = {
        "Etobicoke": 2,
        "York": 1
    }

    assert result == expected


def test_collisions_by_neighbourhood_strips_spaces_and_filters_nsa_unknown():
    df = pd.DataFrame({
        "NEIGHBOURHOOD_158": [
            " Downtown ",
            "NSA",
            "unknown",
            " Scarborough ",
            "DOWNTOWN",
            "Unknown"
        ]
    })

    result = collisions_by_neighbourhood(df)

    expected = {
        "Downtown": 1,
        "Scarborough": 1,
        "DOWNTOWN": 1
    }

    assert result == expected


def test_collisions_by_neighbourhood_raises_keyerror_if_no_neighbourhood_column_exists():
    df = pd.DataFrame({
        "OTHER_COLUMN": [1, 2, 3]
    })

    with pytest.raises(KeyError, match="No neighbourhood column found"):
        collisions_by_neighbourhood(df)



from src.analysis import collisions_by_road_user


def test_collisions_by_road_user_basic():
    data = {
        "AUTOMOBILE": ["YES", "NO", "YES", "N/R"],
        "MOTORCYCLE": ["NO", "YES", "NO", "N/R"],
        "PASSENGER": ["NO", "NO", "NO", "N/R"],
        "BICYCLE": ["YES", "NO", "N/R", "NO"],
        "PEDESTRIAN": ["NO", "YES", "NO", "N/R"],
    }

    df = pd.DataFrame(data)

    result = collisions_by_road_user(df)

    expected = {
        "AUTOMOBILE": 2,
        "MOTORCYCLE": 1,
        "PASSENGER": 0,
        "BICYCLE": 1,
        "PEDESTRIAN": 1,
    }

    assert result == expected