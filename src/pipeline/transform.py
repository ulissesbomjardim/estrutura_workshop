import pandas as pd

"""
função para transformar os dados de uma lista de DataFrames
em um único DataFrame concatenado.

args: data_list (List[pd.DataFrame]): lista de DataFrames

returns: DataFrame concatenado
"""

def transform_data(data_list: list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_list, ignore_index=True)