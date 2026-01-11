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
    
    #This helps to resolve path issue.
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in '{folder_path}'!")
    
    return csv_files