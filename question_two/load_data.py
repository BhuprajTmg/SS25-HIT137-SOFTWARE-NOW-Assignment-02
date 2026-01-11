import os
import pandas as pd
from pathlib import Path
from config import TEMPERATURES_FOLDER


def check_folder_exists(folder_path):
    """
    Check if the data folder exists.
    
    Args:
        folder_path: Path to the folder to check
        
    Raises:
        FileNotFoundError: If folder doesn't exist
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found!")


def get_csv_files(folder_path):
    """
    Get all CSV files from the folder.
    
    Args:
        folder_path: Path to search for CSV files
        
    Returns:
        List of CSV file paths
        
    Raises:
        FileNotFoundError: If no CSV files found
    """
    csv_files = list(Path(folder_path).glob('*.csv'))
    
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in '{folder_path}'!")
    
    return csv_files


def load_single_csv(file_path):
    """
    Load a single CSV file.
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        DataFrame with data, or None if loading fails
    """
    try:
        df = pd.read_csv(file_path)
        print(f"  ✓ Loaded: {file_path.name} ({len(df)} stations)")
        return df
    except Exception as e:
        print(f"  ✗ Warning: Could not load {file_path.name}: {e}")
        return None