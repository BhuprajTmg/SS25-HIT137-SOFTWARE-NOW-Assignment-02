import pandas as pd
from config import SEASON_MAPPING, SEASON_ORDER


def add_season_column(df):
    """
    Add a Season column to the DataFrame based on Month.
    
    Args:
        df: DataFrame with Month column
        
    Returns:
        DataFrame with added Season column
    """
    df = df.copy()
    df['Season'] = df['Month'].map(SEASON_MAPPING)
    df = df.dropna(subset=['Season'])
    return df