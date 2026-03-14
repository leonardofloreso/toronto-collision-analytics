import pandas as pd
from src.analysis import collisions_by_neighbourhood


def test_collisions_by_neighbourhood():

    # create small sample dataset
    data = {
        "NEIGHBOURHOOD": [
            "Downtown",
            "Downtown",
            "Scarborough",
            "Etobicoke",
            "Scarborough"
        ]
    }

    df = pd.DataFrame(data)

    result = collisions_by_neighbourhood(df)

    assert result["Downtown"] == 2
    assert result["Scarborough"] == 2
    assert result["Etobicoke"] == 1