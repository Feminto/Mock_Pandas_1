import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    conditions = (cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')
    return cinema[conditions].sort_values('rating', ascending = False)