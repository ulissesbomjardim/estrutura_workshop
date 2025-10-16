import pandas as pd

"""
função para transformar os dados de uma lista de DataFrames
em um único DataFrame concatenado.

args: data_list (List[pd.DataFrame]): lista de DataFrames

returns: DataFrame concatenado
"""


def transform_data(data_list: list[pd.DataFrame]) -> pd.DataFrame:
    """Concatenate a list of DataFrames into a single DataFrame.

    Args:
        data_list: list of pandas DataFrame objects

    Returns:
        pandas.DataFrame: concatenated dataframe

    Raises:
        ValueError: if data_list is empty
    """

    if not data_list:
        raise ValueError("data_list must contain at least one DataFrame")

    return pd.concat(data_list, ignore_index=True)
