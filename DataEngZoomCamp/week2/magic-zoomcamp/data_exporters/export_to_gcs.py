import os
import pyarrow as pa
import pyarrow.parquet as pq

from pandas import DataFrame


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/personal-gcp.json"

@data_exporter
def export_data_to_google_cloud_storage(taxi_data: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    bucket_name = "dataeng-zoomcamp-demo-bucket"
    table_name = "green_taxi_data_2022"
    root_path = f"{bucket_name}/{table_name}"

    gcs = pa.fs.GcsFileSystem()
    table = pa.Table.from_pandas(taxi_data)

    pq.write_to_dataset(
        table,
        root_path,
        filesystem=gcs,
        partition_cols=["lpep_pickup_date"]
    )
