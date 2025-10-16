import glob
import os
from typing import List

import pandas as pd

"""
função para ler os dados de arquivos *.xslx
no diretório 'data/input' e retornar uma lista de DataFrames.

args: input_path (str): caminho para o diretório de entrada

returns: lista de DataFrames
"""


def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    """Read all .xlsx files from input_path and return a list of DataFrames.

    Args:
        input_path: path to the directory containing .xlsx files

    Returns:
        list of pandas.DataFrame objects
    """

    pattern = os.path.join(input_path, "*.xlsx")
    all_files = glob.glob(pattern)

    data_list: List[pd.DataFrame] = []
    for file_path in all_files:
        df = pd.read_excel(file_path)
        data_list.append(df)

    return data_list


if __name__ == "__main__":
    data_list = extract_from_excel("data/input")
    print(data_list)
