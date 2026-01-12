import pandas as pd


def calculate_station_std(long_df):
    """
    Calculate standard deviation for each station.
    Lower std = more stable temperatures
    Higher std = more variable temperatures
    
    Args:
        long_df: DataFrame in long format
        
    Returns:
        Series with station standard deviations
    """
    # Remove NaN temperatures
    df = long_df.dropna(subset=['Temperature'])
    
    # Calculate std for each station
    station_std = df.groupby('Station')['Temperature'].std()
    
    return station_std