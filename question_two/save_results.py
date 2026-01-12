import os
from config import SEASON_ORDER


def ensure_output_folder(filepath):
    """
    Ensure the output folder exists.
    
    Args:
        filepath: Path to output file
    """
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)