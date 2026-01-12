import pandas as pd
from config import MONTH_COLUMNS, STATION_COLUMN_NAMES


def identify_station_column(df):
    """
    Identify station column to handle varying CSV formats.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Name of the station identifier column
        
    Raises:
        ValueError: If no valid station column found
    """
    for column_name in STATION_COLUMN_NAMES:
        if column_name in df.columns:
            return column_name
    
    raise ValueError(
        f"Could not identify station column. "
        f"Expected one of: {STATION_COLUMN_NAMES}. "
        f"Found columns: {list(df.columns)}"
    )


def validate_month_columns(df):
    """
    Validate presence of month columns to ensure data quality.
    
    Args:
        df: Input DataFrame
        
    Returns:
        List of available month columns
        
    Raises:
        ValueError: If no month columns found
    """
    available_months = [col for col in MONTH_COLUMNS if col in df.columns]
    
    if not available_months:
        raise ValueError(
            f"No month columns found in CSV. "
            f"Expected: {MONTH_COLUMNS}. "
            f"Found: {list(df.columns)}"
        )
    
    # Warn if some months are missing to alert user of incomplete data
    missing_months = set(MONTH_COLUMNS) - set(available_months)
    if missing_months:
        print(f"  ⚠ Note: Missing month columns: {missing_months}")
    
    return available_months


def transform_to_long_format(df):
    """
    Transform wide format to long format for easier analysis.
    Wide: Each row = station, months = columns
    Long: Each row = one temperature reading
    
    Args:
        df: DataFrame in wide format
        
    Returns:
        DataFrame in long format (Station, Month, Temperature)
        
    Raises:
        ValueError: If transformation fails due to data issues
    """
    print("Transforming data to long format...")
    
    station_col = identify_station_column(df)
    month_cols = validate_month_columns(df)
    
    try:
        long_df = pd.melt(
            df,
            id_vars=[station_col],
            value_vars=month_cols,
            var_name='Month',
            value_name='Temperature'
        )
    except KeyError as e:
        raise ValueError(f"Column error during transformation: {e}")
    
    long_df = long_df.rename(columns={station_col: 'Station'})
    
    initial_count = len(long_df)
    long_df = long_df.dropna(subset=['Temperature'])
    removed_count = initial_count - len(long_df)
    
    if removed_count > 0:
        print(f"  Removed {removed_count} records with missing temperatures")
    
    if long_df.empty:
        raise ValueError("No valid temperature data after transformation")
    
    print(f"  Transformed: {len(long_df)} temperature records\n")
    
    return long_df