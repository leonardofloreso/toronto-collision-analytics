import pandas as pd
from matplotlib.figure import Figure
from analytics import collisions_by_weekday, plot_collisions_by_weekday


def test_collisions_by_weekday_counts_correctly():
    df = pd.DataFrame({
        "OCC_DOW": ["Mon", "Mon", "Tue", "Fri", "Fri", "Fri"]
    })

    result = collisions_by_weekday(df)
    result_dict = dict(zip(result["OCC_DOW"], result["collision_count"]))

    assert result_dict["Mon"] == 2
    assert result_dict["Tue"] == 1
    assert result_dict["Fri"] == 3


def test_collisions_by_weekday_fills_missing_days_with_zero():
    df = pd.DataFrame({
        "OCC_DOW": ["Wed", "Wed"]
    })

    result = collisions_by_weekday(df)
    result_dict = dict(zip(result["OCC_DOW"], result["collision_count"]))

    assert result_dict["Wed"] == 2
    assert result_dict["Mon"] == 0
    assert result_dict["Tue"] == 0
    assert result_dict["Thu"] == 0
    assert result_dict["Fri"] == 0
    assert result_dict["Sat"] == 0
    assert result_dict["Sun"] == 0


def test_plot_collisions_by_weekday_returns_figure():
    weekday_data = pd.DataFrame({
        "OCC_DOW": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "collision_count": [10, 12, 9, 8, 15, 7, 5]
    })

    fig = plot_collisions_by_weekday(weekday_data)

    assert isinstance(fig, Figure)