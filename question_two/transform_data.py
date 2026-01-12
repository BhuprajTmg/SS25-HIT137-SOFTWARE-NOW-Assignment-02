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


def get_available_months(df):
    """
    Get list of month columns that exist in the DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        List of month column names
        
    Raises:
        ValueError: If no month columns found
    """
    available_months = [col for col in MONTH_COLUMNS if col in df.columns]
    
    if not available_months:
        raise ValueError(f"No month columns found! Expected: {MONTH_COLUMNS}")
    
    return available_months