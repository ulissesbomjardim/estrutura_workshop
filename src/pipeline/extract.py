import os
import glob

import pandas as pd

from typing import List

"""
função para ler os dados de arquivos *.xslx 
no diretório 'data/input' e retornar uma lista de DataFrames.

args: input_path (str): caminho para o diretório de entrada

returns: lista de DataFrames
"""

def extract_fron_excel(input_path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(input_path, "*.xlsx"))
       
    data_list = []
    for file in all_files:
        data_list.append(pd.read_excel(file))
            
    return data_list

if __name__ == "__main__":
    data_list = extract_fron_excel("data/input")
    print(data_list)