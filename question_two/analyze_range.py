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


def find_largest_range_stations(long_df):
    """
    Find station(s) with the largest temperature range.
    Handles ties by returning all stations with maximum range.
    
    Args:
        long_df: DataFrame in long format
        
    Returns:
        List of dictionaries with station info
    """
    print("Finding largest temperature range...")
    
    # Calculate ranges
    station_stats = calculate_station_ranges(long_df)
    
    # Find maximum range
    max_range = station_stats['range'].max()
    
    # Get all stations with max range
    max_stations = station_stats[station_stats['range'] == max_range]
    
    # Format results
    results = []
    for station, row in max_stations.iterrows():
        results.append({
            'station': station,
            'range': row['range'],
            'max': row['max'],
            'min': row['min']
        })
        print(f"  {station}: Range {row['range']:.1f}°C")
    
    print()
    return results