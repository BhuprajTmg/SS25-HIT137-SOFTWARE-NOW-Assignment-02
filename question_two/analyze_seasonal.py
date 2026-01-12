import pandas as pd
from config import SEASON_MAPPING, SEASON_ORDER, OUTPUT_PRECISION


def validate_dataframe(df):
    """
    Validate DataFrame has required columns for analysis.
    
    Args:
        df: DataFrame to validate
        
    Raises:
        ValueError: If required columns missing
    """
    required_cols = ['Month', 'Temperature']
    missing = [col for col in required_cols if col not in df.columns]
    
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    if df.empty:
        raise ValueError("DataFrame is empty, cannot perform analysis")


def map_months_to_seasons(df):
    """
    Add season column based on month to enable seasonal grouping.
    
    Args:
        df: DataFrame with Month column
        
    Returns:
        DataFrame with Season column added
    """
    df = df.copy()
    df['Season'] = df['Month'].map(SEASON_MAPPING)
    
    # Remove rows where season mapping failed (invalid month names)
    invalid_count = df['Season'].isna().sum()
    if invalid_count > 0:
        print(f"  ⚠ Warning: {invalid_count} records with invalid month names")
    
    df = df.dropna(subset=['Season'])
    
    if df.empty:
        raise ValueError("No valid season mappings found")
    
    return df


def calculate_seasonal_averages(long_df):
    """
    Calculate mean temperature for each season across all stations and years.
    
    Args:
        long_df: DataFrame in long format
        
    Returns:
        Dictionary mapping season names to average temperatures
        
    Raises:
        ValueError: If calculation fails
    """
    print("Calculating seasonal averages...")
    
    validate_dataframe(long_df)
    df_with_seasons = map_months_to_seasons(long_df)
    
    try:
        seasonal_means = df_with_seasons.groupby('Season')['Temperature'].mean()
    except KeyError as e:
        raise ValueError(f"Error calculating seasonal means: {e}")
    
    result = {}
    for season in SEASON_ORDER:
        if season in seasonal_means:
            temp = seasonal_means[season]
            result[season] = temp
            print(f"  {season}: {temp:.{OUTPUT_PRECISION}f}°C")
        else:
            result[season] = None
            print(f"  {season}: No data")
    
    print()
    return result