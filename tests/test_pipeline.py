import pandas as pd
from src.pipeline.transform import transform_data

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})

df2 = pd.DataFrame({
    'A': [4, 5, 6],
    'B': ['d', 'e', 'f']
})



def test_concat_list_of_dataframes():
    arrange = pd.concat([df1, df2], ignore_index=True)
    
    act = transform_data([df1, df2])

    assert act.equals(arrange)