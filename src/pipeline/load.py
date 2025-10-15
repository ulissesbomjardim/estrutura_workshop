import pandas as pd
import os

"""
função para transformar um dataframe em um arquivo xlsx.

args: 
    df (pd.DataFrame): DataFrame a ser salvo
    output_path (str): caminho para salvar o arquivo
    filename (str): nome do arquivo a ser salvo
      
returns: "arquivo xlsx salvo com sucesso"
"""

def load_to_excel(df: pd.DataFrame, output_path: str, filename: str) -> str:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    df.to_excel(f"{output_path}/{filename}.xlsx", index=False)
    return "arquivo xlsx salvo com sucesso"