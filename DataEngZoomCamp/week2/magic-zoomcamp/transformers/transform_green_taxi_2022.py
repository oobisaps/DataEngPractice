import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(taxi_data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    def camel_to_snake(column_name: str) -> str:
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', column_name).lower()

    taxi_data["lpep_pickup_date"] = taxi_data["lpep_pickup_datetime"].dt.date
    taxi_data = taxi_data.rename(columns=lambda x: camel_to_snake(x))

    return taxi_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
