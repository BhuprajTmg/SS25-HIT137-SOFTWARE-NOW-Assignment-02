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


def save_seasonal_averages(seasonal_avg, output_file):
    """
    Save seasonal averages to file.
    Format: "Season: XX.X°C"
    
    Args:
        seasonal_avg: Dictionary with seasonal averages
        output_file: Path to output file
    """
    ensure_output_folder(output_file)
    
    with open(output_file, 'w') as f:
        for season in SEASON_ORDER:
            if seasonal_avg[season] is not None:
                f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")
            else:
                f.write(f"{season}: No data\n")
    
    print(f"✓ Saved: {output_file}")


def save_stability_results(stable_stations, variable_stations, output_file):
    """
    Save temperature stability results to file.
    Format: "Most Stable: Station XXX: StdDev XX.X°C"
            "Most Variable: Station XXX: StdDev XX.X°C"
    
    Args:
        stable_stations: List of most stable stations
        variable_stations: List of most variable stations
        output_file: Path to output file
    """
    ensure_output_folder(output_file)
    
    with open(output_file, 'w') as f:
        # Write most stable
        for station_info in stable_stations:
            station = station_info['station']
            std = station_info['std']
            f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")
        
        # Write most variable
        for station_info in variable_stations:
            station = station_info['station']
            std = station_info['std']
            f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")
    
    print(f"✓ Saved: {output_file}")


def save_range_results(range_stations, output_file):
    """
    Save temperature range results to file.
    Format: "Station XXX: Range XX.X°C (Max: XX.X°C, Min: XX.X°C)"
    
    Args:
        range_stations: List of dictionaries with station info
        output_file: Path to output file
    """
    ensure_output_folder(output_file)
    
    with open(output_file, 'w') as f:
        for station_info in range_stations:
            station = station_info['station']
            temp_range = station_info['range']
            max_temp = station_info['max']
            min_temp = station_info['min']
            
            line = (f"Station {station}: Range {temp_range:.1f}°C "
                   f"(Max: {max_temp:.1f}°C, Min: {min_temp:.1f}°C)\n")
            f.write(line)
    
    print(f"✓ Saved: {output_file}")