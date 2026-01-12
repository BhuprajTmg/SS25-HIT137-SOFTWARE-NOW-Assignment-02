import pandas as pd
from config import OUTPUT_PRECISION


def validate_temperature_data(df):
    """
    Validate DataFrame for temperature range analysis.
    
    Args:
        df: DataFrame to validate
        
    Raises:
        ValueError: If data is invalid for analysis
    """
    required_cols = ['Station', 'Temperature']
    missing = [col for col in required_cols if col not in df.columns]
    
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    if df.empty:
        raise ValueError("No data available for range analysis")


def compute_station_statistics(df):
    """
    Compute min, max, and range for each station.
    Range calculation helps identify climate variability.
    
    Args:
        df: DataFrame with temperature data
        
    Returns:
        DataFrame with statistics per station
        
    Raises:
        ValueError: If computation fails
    """
    df_clean = df.dropna(subset=['Temperature'])
    
    if df_clean.empty:
        raise ValueError("No valid temperature data after removing NaN values")
    
    try:
        stats = df_clean.groupby('Station')['Temperature'].agg(['min', 'max'])
        stats['range'] = stats['max'] - stats['min']
    except KeyError as e:
        raise ValueError(f"Error computing statistics: {e}")
    
    return stats


def find_largest_range_stations(long_df):
    """
    Find stations with maximum temperature range.
    Handles ties by returning all stations with the same maximum range.
    
    Args:
        long_df: DataFrame in long format
        
    Returns:
        List of dictionaries with station information
        
    Raises:
        ValueError: If analysis cannot be completed
    """
    print("Finding largest temperature range...")
    
    validate_temperature_data(long_df)
    station_stats = compute_station_statistics(long_df)
    
    max_range = station_stats['range'].max()
    
    if pd.isna(max_range):
        raise ValueError("Could not calculate maximum range")
    
    max_stations = station_stats[station_stats['range'] == max_range]
    
    results = []
    for station, row in max_stations.iterrows():
        results.append({
            'station': station,
            'range': row['range'],
            'max': row['max'],
            'min': row['min']
        })
        print(f"  {station}: Range {row['range']:.{OUTPUT_PRECISION}f}°C")
    
    print()
    return results