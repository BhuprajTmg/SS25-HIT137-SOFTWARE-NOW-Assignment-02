import pandas as pd


def calculate_station_ranges(long_df):
    """
    Calculate temperature range for each station.
    Range = Maximum temperature - Minimum temperature
    
    Args:
        long_df: DataFrame in long format
        
    Returns:
        DataFrame with columns: Station, min, max, range
    """
    # Remove NaN temperatures
    df = long_df.dropna(subset=['Temperature'])
    
    # Calculate min, max, and range for each station
    station_stats = df.groupby('Station')['Temperature'].agg(['min', 'max'])
    station_stats['range'] = station_stats['max'] - station_stats['min']
    
    return station_stats