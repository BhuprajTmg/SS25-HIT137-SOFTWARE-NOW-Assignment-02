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


def transform_to_long_format(df):
    """
    Transform data from wide format to long format.
    
    Wide format: Each row is a station, months are columns
    Long format: Each row is one temperature reading
    
    Args:
        df: DataFrame in wide format
        
    Returns:
        DataFrame in long format with columns: Station, Month, Temperature
    """
    print("Transforming data to long format...")
    
    # Find station column
    station_col = find_station_column(df)
    
    # Get available month columns
    month_cols = get_available_months(df)
    
    # Melt the DataFrame
    long_df = pd.melt(
        df,
        id_vars=[station_col],
        value_vars=month_cols,
        var_name='Month',
        value_name='Temperature'
    )
    
    # Rename station column
    long_df = long_df.rename(columns={station_col: 'Station'})
    
    # Remove NaN temperatures
    initial_count = len(long_df)
    long_df = long_df.dropna(subset=['Temperature'])
    removed = initial_count - len(long_df)
    
    if removed > 0:
        print(f"  Removed {removed} records with missing temperatures")
    
    print(f"  Transformed: {len(long_df)} temperature records\n")
    
    return long_df