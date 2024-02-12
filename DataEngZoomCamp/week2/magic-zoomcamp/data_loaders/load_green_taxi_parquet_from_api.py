import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{}.parquet'

    taxi_data = None
    for month in range(1, 13):
        
        if month < 10:
            month_str = f"0{month}"
        else:
            month_str = str(month)
        
        month_data = pd.read_parquet(
            url.format(month_str),
        )

        if taxi_data is not None:
            taxi_data = pd.concat([taxi_data, month_data], axis=0)
        else:
            taxi_data = month_data

    return taxi_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
