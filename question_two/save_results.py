import os
from config import SEASON_ORDER, OUTPUT_PRECISION


def ensure_output_directory(filepath):
    """
    Create output directory if needed to prevent write failures.
    
    Args:
        filepath: Full path to output file
    """
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            raise OSError(f"Cannot create output directory: {e}")


def validate_file_writable(filepath):
    """
    Check if file can be written to avoid silent failures.
    
    Args:
        filepath: Path to check
        
    Raises:
        PermissionError: If file cannot be written
    """
    directory = os.path.dirname(filepath) or '.'
    
    if not os.access(directory, os.W_OK):
        raise PermissionError(
            f"No write permission for directory: {directory}"
        )


# def save_seasonal_averages(seasonal_avg, output_file):
#     """
#     Write seasonal averages to file in specified format.
    
#     Args:
#         seasonal_avg: Dictionary of seasonal averages
#         output_file: Output file path
        
#     Raises:
#         ValueError: If seasonal_avg is invalid
#         OSError: If file write fails
#     """
#     if not isinstance(seasonal_avg, dict):
#         raise ValueError("seasonal_avg must be a dictionary")
    
#     ensure_output_directory(output_file)
#     validate_file_writable(output_file)
    
#     try:
#         with open(output_file, 'w') as f:
#             for season in SEASON_ORDER:
#                 temp = seasonal_avg.get(season)
#                 if temp is not None:
#                     f.write(f"{season}: {temp:.{OUTPUT_PRECISION}f}°C\n")
#                 else:
#                     f.write(f"{season}: No data\n")
#     except IOError as e:
#         raise OSError(f"Failed to write {output_file}: {e}")
    
#     print(f"✓ Saved: {output_file}")


def save_seasonal_averages(seasonal_avg, output_file):
    """
    Write seasonal averages to file in specified format.
    
    Args:
        seasonal_avg: Dictionary of seasonal averages
        output_file: Output file path
        
    Raises:
        ValueError: If seasonal_avg is invalid
        OSError: If file write fails
    """
    if not isinstance(seasonal_avg, dict):
        raise ValueError("seasonal_avg must be a dictionary")
    
    ensure_output_directory(output_file)
    validate_file_writable(output_file)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f: 
            for season in SEASON_ORDER:
                temp = seasonal_avg.get(season)
                if temp is not None:
                    f.write(f"{season}: {temp:.{OUTPUT_PRECISION}f}°C\n")
                else:
                    f.write(f"{season}: No data\n")
    except IOError as e:
        raise OSError(f"Failed to write {output_file}: {e}")
    
    print(f"✓ Saved: {output_file}")


def save_range_results(range_stations, output_file):
    """
    Write temperature range results to file.
    
    Args:
        range_stations: List of station dictionaries
        output_file: Output file path
        
    Raises:
        ValueError: If range_stations is invalid
        OSError: If file write fails
    """
    if not isinstance(range_stations, list):
        raise ValueError("range_stations must be a list")
    
    if not range_stations:
        raise ValueError("range_stations is empty")
    
    ensure_output_directory(output_file)
    validate_file_writable(output_file)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for station_info in range_stations:
                station = station_info['station']
                temp_range = station_info['range']
                max_temp = station_info['max']
                min_temp = station_info['min']
                
                line = (
                    f"Station {station}: "
                    f"Range {temp_range:.{OUTPUT_PRECISION}f}°C "
                    f"(Max: {max_temp:.{OUTPUT_PRECISION}f}°C, "
                    f"Min: {min_temp:.{OUTPUT_PRECISION}f}°C)\n"
                )
                f.write(line)
    except (IOError, KeyError) as e:
        raise OSError(f"Failed to write {output_file}: {e}")
    
    print(f"✓ Saved: {output_file}")


def save_stability_results(stable_stations, variable_stations, output_file):
    """
    Write temperature stability results to file.
    
    Args:
        stable_stations: List of most stable stations
        variable_stations: List of most variable stations
        output_file: Output file path
        
    Raises:
        ValueError: If input data is invalid
        OSError: If file write fails
    """
    if not isinstance(stable_stations, list) or not isinstance(variable_stations, list):
        raise ValueError("Station lists must be lists")
    
    if not stable_stations or not variable_stations:
        raise ValueError("Station lists cannot be empty")
    
    ensure_output_directory(output_file)
    validate_file_writable(output_file)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for station_info in stable_stations:
                station = station_info['station']
                std = station_info['std']
                f.write(
                    f"Most Stable: Station {station}: "
                    f"StdDev {std:.{OUTPUT_PRECISION}f}°C\n"
                )
            
            for station_info in variable_stations:
                station = station_info['station']
                std = station_info['std']
                f.write(
                    f"Most Variable: Station {station}: "
                    f"StdDev {std:.{OUTPUT_PRECISION}f}°C\n"
                )
    except (IOError, KeyError) as e:
        raise OSError(f"Failed to write {output_file}: {e}")
    
    print(f"✓ Saved: {output_file}")