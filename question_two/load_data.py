import os
import pandas as pd
from pathlib import Path
from config import TEMPERATURES_FOLDER


def validate_folder_exists(folder_path):
    """
    Validate folder existence to provide clear error messages early.
    
    Args:
        folder_path: Path to validate
        
    Raises:
        FileNotFoundError: If folder does not exist
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(
            f"Data folder '{folder_path}' not found. "
            f"Please create it and add CSV files."
        )
    
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(
            f"'{folder_path}' exists but is not a directory."
        )


def discover_csv_files(folder_path):
    """
    Discover all CSV files in the specified folder.
    
    Args:
        folder_path: Path to search
        
    Returns:
        List of Path objects for discovered CSV files
        
    Raises:
        FileNotFoundError: If no CSV files found
    """
    csv_files = list(Path(folder_path).glob('*.csv'))
    
    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in '{folder_path}'. "
            f"Please add CSV files with temperature data."
        )
    
    return csv_files


def load_csv_file(file_path):
    """
    Load a single CSV file with error handling.
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        DataFrame if successful, None if loading fails
    """
    try:
        df = pd.read_csv(file_path)
        
        # Validate that DataFrame is not empty
        if df.empty:
            print(f"  ⚠ Warning: {file_path.name} is empty, skipping")
            return None
        
        print(f"  ✓ Loaded: {file_path.name} ({len(df)} stations)")
        return df
        
    except pd.errors.EmptyDataError:
        print(f"  ✗ Error: {file_path.name} is empty or malformed")
        return None
    except pd.errors.ParserError as e:
        print(f"  ✗ Error: Could not parse {file_path.name}: {e}")
        return None
    except Exception as e:
        print(f"  ✗ Error: Unexpected error loading {file_path.name}: {e}")
        return None


def load_all_temperature_data():
    """
    Load and combine all CSV files from the temperatures folder.
    
    Returns:
        Combined DataFrame with all temperature data
        
    Raises:
        FileNotFoundError: If folder or files not found
        ValueError: If no data could be loaded successfully
    """
    print(f"Loading data from '{TEMPERATURES_FOLDER}'...")
    
    validate_folder_exists(TEMPERATURES_FOLDER)
    csv_files = discover_csv_files(TEMPERATURES_FOLDER)
    
    print(f"Found {len(csv_files)} CSV file(s)\n")
    
    loaded_dataframes = []
    
    for file_path in csv_files:
        df = load_csv_file(file_path)
        if df is not None:
            loaded_dataframes.append(df)
    
    # Ensure at least one file loaded successfully
    if not loaded_dataframes:
        raise ValueError(
            "No data could be loaded. Please check CSV file formats."
        )
    
    combined_df = pd.concat(loaded_dataframes, ignore_index=True)
    print(f"\nTotal stations loaded: {len(combined_df)}")
    print(f"Total records: {len(combined_df) * 12} temperature readings\n")
    
    return combined_df