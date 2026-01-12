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


def find_most_stable(station_std):
    """
    Find station(s) with lowest standard deviation (most stable).
    
    Args:
        station_std: Series of standard deviations
        
    Returns:
        List of dictionaries with station and std
    """
    min_std = station_std.min()
    most_stable = station_std[station_std == min_std]
    
    results = []
    for station, std in most_stable.items():
        results.append({'station': station, 'std': std})
    
    return results


def find_most_variable(station_std):
    """
    Find station(s) with highest standard deviation (most variable).
    
    Args:
        station_std: Series of standard deviations
        
    Returns:
        List of dictionaries with station and std
    """
    max_std = station_std.max()
    most_variable = station_std[station_std == max_std]
    
    results = []
    for station, std in most_variable.items():
        results.append({'station': station, 'std': std})
    
    return results