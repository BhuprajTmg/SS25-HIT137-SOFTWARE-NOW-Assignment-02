import pandas as pd
from config import MONTH_COLUMNS


def find_station_column(df):
    """
    Find the station identifier column in the DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Name of the station column
        
    Raises:
        ValueError: If no station column found
    """
    possible_names = ['STATION_NAME', 'Station', 'STN_ID', 'station_name']
    
    for col_name in possible_names:
        if col_name in df.columns:
            return col_name
    
    raise ValueError("Could not find station column!")