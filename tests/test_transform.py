import pandas as pd
import pytest

from src.pipeline.transform import transform_data


def test_concat_two_dataframes():
    df1 = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    df2 = pd.DataFrame({"A": [3, 4], "B": ["z", "w"]})

    expected = pd.concat([df1, df2], ignore_index=True)
    result = transform_data([df1, df2])

    assert result.equals(expected)


def test_single_dataframe_returns_same_dataframe():
    df = pd.DataFrame({"A": [1], "B": ["a"]})

    expected = pd.concat([df], ignore_index=True)
    result = transform_data([df])

    assert result.equals(expected)


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        transform_data([])


def test_concat_different_columns_creates_union_and_fills_nan():
    df1 = pd.DataFrame({"A": [1], "B": ["a"]})
    df2 = pd.DataFrame({"A": [2], "C": [True]})

    expected = pd.concat([df1, df2], ignore_index=True)
    result = transform_data([df1, df2])

    # comparar colunas e valores (NaN é esperado onde não há valor)
    assert list(result.columns) == list(expected.columns)
    assert result.equals(expected)


import pandas as pd
import pytest

from src.pipeline.transform import transform_data


def test_concat_two_dataframes():
    df1 = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    df2 = pd.DataFrame({"A": [3, 4], "B": ["z", "w"]})

    expected = pd.concat([df1, df2], ignore_index=True)
    result = transform_data([df1, df2])

    assert result.equals(expected)


def test_single_dataframe_returns_same_dataframe():
    df = pd.DataFrame({"A": [1], "B": ["a"]})

    expected = pd.concat([df], ignore_index=True)
    result = transform_data([df])

    assert result.equals(expected)


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        transform_data([])


def test_concat_different_columns_creates_union_and_fills_nan():
    df1 = pd.DataFrame({"A": [1], "B": ["a"]})
    df2 = pd.DataFrame({"A": [2], "C": [True]})

    expected = pd.concat([df1, df2], ignore_index=True)
    result = transform_data([df1, df2])

    # comparar colunas e valores (NaN é esperado onde não há valor)
    assert list(result.columns) == list(expected.columns)
    assert result.equals(expected)
