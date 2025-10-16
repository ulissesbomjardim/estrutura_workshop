import os

import pandas as pd

"""
função para transformar um dataframe em um arquivo xlsx.

args:
    df (pd.DataFrame): DataFrame a ser salvo
    output_path (str): caminho para salvar o arquivo
    filename (str): nome do arquivo a ser salvo

returns: "arquivo xlsx salvo com sucesso"
"""


def load_to_excel(df: pd.DataFrame, output_path: str, filename: str) -> str:
    """Save DataFrame to an xlsx file.

    Args:
        df: DataFrame to save
        output_path: directory to save the file
        filename: filename without extension

    Returns:
        success message string
    """

    os.makedirs(output_path, exist_ok=True)

    out_path = os.path.join(output_path, f"{filename}.xlsx")
    df.to_excel(out_path, index=False)
    return "arquivo xlsx salvo com sucesso"
