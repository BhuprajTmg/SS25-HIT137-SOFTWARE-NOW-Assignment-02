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


def main():
    """
    Main execution function.
    Coordinates all analysis steps.
    """
    try:
        print_header()
        
        # Step 1: Load data
        print("[Step 1/5] Loading temperature data...")
        df = load_all_temperature_data()
        
        # Step 2: Transform data
        print("[Step 2/5] Transforming data...")
        long_df = transform_to_long_format(df)
        
        # Step 3: Seasonal averages
        print("[Step 3/5] Analyzing seasonal averages...")
        seasonal_avg = calculate_seasonal_averages(long_df.copy())
        save_seasonal_averages(seasonal_avg, OUTPUT_SEASONAL_AVG)
        print()
        
        # Step 4: Temperature range
        print("[Step 4/5] Finding largest temperature ranges...")
        range_stations = find_largest_range_stations(long_df.copy())
        save_range_results(range_stations, OUTPUT_TEMP_RANGE)
        print()






def handle_error(error):
    """
    Handle and display errors appropriately.
    
    Args:
        error: The exception that occurred
    """
    print("\n" + "=" * 70)
    print("✗ Error occurred!")
    print("=" * 70)
    print(f"\nError: {error}")
    print("\nPlease check:")
    print("  1. 'temperatures' folder exists")
    print("  2. CSV files are present")
    print("  3. CSV files have correct format")
    print("  4. Required columns: STATION_NAME, January-December")
    print("=" * 70)
    print(" " * 18 + "Temperature Analysis Program")
    print("=" * 70)
    print()


def print_footer():
    """Print success footer."""
    print("=" * 70)
    print("✓ Analysis Complete!")
    print()
    print("Output files created:")
    print(f"  • {OUTPUT_SEASONAL_AVG}")
    print(f"  • {OUTPUT_TEMP_RANGE}")
    print(f"  • {OUTPUT_TEMP_STABILITY}")
    print("=" * 70)