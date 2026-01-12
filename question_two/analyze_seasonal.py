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


def calculate_seasonal_averages(long_df):
    """
    Calculate average temperature for each season.
    Averages across all stations and all data.
    
    Args:
        long_df: DataFrame in long format (Station, Month, Temperature)
        
    Returns:
        Dictionary with seasonal averages
    """
    print("Calculating seasonal averages...")
    
    # Add season column
    df_with_seasons = add_season_column(long_df)
    
    # Calculate mean for each season
    seasonal_means = df_with_seasons.groupby('Season')['Temperature'].mean()
    
    # Create result dictionary in correct order
    result = {}
    for season in SEASON_ORDER:
        if season in seasonal_means:
            result[season] = seasonal_means[season]
            print(f"  {season}: {seasonal_means[season]:.1f}°C")
        else:
            result[season] = None
            print(f"  {season}: No data")
    
    print()
    return result