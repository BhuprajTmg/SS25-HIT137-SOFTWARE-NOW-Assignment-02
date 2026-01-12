from load_data import load_all_temperature_data
from transform_data import transform_to_long_format
from analyze_seasonal import calculate_seasonal_averages
from analyze_range import find_largest_range_stations
from analyze_stability import analyze_temperature_stability
from save_results import (
    save_seasonal_averages,
    save_range_results,
    save_stability_results
)
from config import (
    OUTPUT_SEASONAL_AVG,
    OUTPUT_TEMP_RANGE,
    OUTPUT_TEMP_STABILITY
)


def print_header():
    """Print program header."""
    print("=" * 70)
    print(" " * 18 + "Temperature Analysis Program")
    print("=" * 70)
    print()