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