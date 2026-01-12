import pandas as pd
from config import OUTPUT_PRECISION


def validate_stability_data(df):
    """
    Validate data for stability analysis.
    
    Args:
        df: DataFrame to validate
        
    Raises:
        ValueError: If data is insufficient
    """
    required_cols = ['Station', 'Temperature']
    missing = [col for col in required_cols if col not in df.columns]
    
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    df_clean = df.dropna(subset=['Temperature'])
    
    if df_clean.empty:
        raise ValueError("No valid temperature data for stability analysis")
    
    # Need at least 2 data points per station for meaningful std deviation
    station_counts = df_clean.groupby('Station').size()
    insufficient = station_counts[station_counts < 2]
    
    if len(insufficient) == len(station_counts):
        raise ValueError("Insufficient data points per station for stability analysis")


def calculate_standard_deviations(df):
    """
    Calculate standard deviation for each station.
    Lower std = more stable (consistent) temperatures.
    Higher std = more variable (fluctuating) temperatures.
    
    Args:
        df: DataFrame with temperature data
        
    Returns:
        Series of standard deviations per station
        
    Raises:
        ValueError: If calculation fails
    """
    df_clean = df.dropna(subset=['Temperature'])
    
    try:
        station_std = df_clean.groupby('Station')['Temperature'].std()
    except KeyError as e:
        raise ValueError(f"Error calculating standard deviations: {e}")
    
    # Remove any NaN results (stations with only one data point)
    station_std = station_std.dropna()
    
    if station_std.empty:
        raise ValueError("Could not calculate any valid standard deviations")
    
    return station_std


def extract_extreme_stations(station_std):
    """
    Extract most stable and most variable stations.
    Handles ties appropriately.
    
    Args:
        station_std: Series of standard deviations
        
    Returns:
        Tuple of (stable_list, variable_list)
    """
    min_std = station_std.min()
    max_std = station_std.max()
    
    most_stable = station_std[station_std == min_std]
    most_variable = station_std[station_std == max_std]
    
    stable_results = [
        {'station': station, 'std': std} 
        for station, std in most_stable.items()
    ]
    
    variable_results = [
        {'station': station, 'std': std} 
        for station, std in most_variable.items()
    ]
    
    return stable_results, variable_results


def analyze_temperature_stability(long_df):
    """
    Perform complete stability analysis.
    
    Args:
        long_df: DataFrame in long format
        
    Returns:
        Tuple of (most_stable, most_variable) station lists
        
    Raises:
        ValueError: If analysis cannot be completed
    """
    print("Analyzing temperature stability...")
    
    validate_stability_data(long_df)
    station_std = calculate_standard_deviations(long_df)
    stable, variable = extract_extreme_stations(station_std)
    
    stable_names = ', '.join([s['station'] for s in stable])
    variable_names = ', '.join([v['station'] for v in variable])
    
    print(f"  Most Stable: {stable_names}")
    print(f"  Most Variable: {variable_names}")
    print()
    
    return stable, variable