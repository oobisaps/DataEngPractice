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

    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_{}-{}.csv.gz'

    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }
    
    parse_date_list = [
        "lpep_pickup_datetime",
        "lpep_dropoff_datetime"
    ]

    taxi_data = None
    for year in ["2019", "2020", "2021"]:
        for month in range(1, 13):

            if month < 10:
                month_ph = f"0{month}"
            else:
                month_ph = str(month)

            if year == 2021 and month > 7:
                break

            url_str = url.format(year, month_ph),

            month_data = pd.read_csv(
                url_str,
                compression="gzip",
                dtype=taxi_dtypes,
                parse_dates=parse_date_list
            )
        
            print(f"{url_str} - {len(month_data)}")

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
