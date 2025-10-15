import os
from pathlib import Path

import pandas as pd
import pandas.testing as pdt
import pytest

from src.pipeline.load import load_to_excel

def test_load_to_excel_creates_file_and_returns_message(tmp_path):
    df = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
    out_dir = tmp_path / "out"
    filename = "test_file"

    msg = load_to_excel(df, str(out_dir), filename)

    assert msg == "arquivo xlsx salvo com sucesso"
    saved = out_dir / f"{filename}.xlsx"
    assert saved.exists()

    read_df = pd.read_excel(saved)
    pdt.assert_frame_equal(df.reset_index(drop=True), read_df)

def test_load_to_excel_creates_nested_dir_if_missing(tmp_path):
    df = pd.DataFrame({'A': [3], 'B': ['z']})
    out_dir = tmp_path / "nested" / "dir"
    filename = "f2"

    # ensure directory does not exist beforehand
    assert not out_dir.exists()

    load_to_excel(df, str(out_dir), filename)

    saved = out_dir / f"{filename}.xlsx"
    assert saved.exists()

import os
from pathlib import Path

import pandas as pd
import pandas.testing as pdt
import pytest

from src.pipeline.load import load_to_excel

def test_load_to_excel_creates_file_and_returns_message(tmp_path):
    df = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
    out_dir = tmp_path / "out"
    filename = "test_file"

    msg = load_to_excel(df, str(out_dir), filename)

    assert msg == "arquivo xlsx salvo com sucesso"
    saved = out_dir / f"{filename}.xlsx"
    assert saved.exists()

    read_df = pd.read_excel(saved)
    pdt.assert_frame_equal(df.reset_index(drop=True), read_df)

def test_load_to_excel_creates_nested_dir_if_missing(tmp_path):
    df = pd.DataFrame({'A': [3], 'B': ['z']})
    out_dir = tmp_path / "nested" / "dir"
    filename = "f2"

    # ensure directory does not exist beforehand
    assert not out_dir.exists()

    load_to_excel(df, str(out_dir), filename)

    saved = out_dir / f"{filename}.xlsx"
    assert saved.exists()