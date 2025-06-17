import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers['count'] = 1
    df = my_numbers.groupby('num')['count'].sum().reset_index()

    condition = (df['count'] == 1)
    df = df[condition]

    result = df['num'].max()
    return pd.DataFrame([result], columns = ['num'])
    # return my_numbers