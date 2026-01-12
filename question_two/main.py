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


def display_header():
    """Display program header for user feedback."""
    print("=" * 70)
    print(" " * 18 + "Temperature Analysis Program")
    print("=" * 70)
    print()


def display_footer():
    """Display success message with output file locations."""
    print("=" * 70)
    print("✓ Analysis Complete!")
    print()
    print("Output files created:")
    print(f"  • {OUTPUT_SEASONAL_AVG}")
    print(f"  • {OUTPUT_TEMP_RANGE}")
    print(f"  • {OUTPUT_TEMP_STABILITY}")
    print("=" * 70)


def display_error(error):
    """
    Display formatted error message with troubleshooting guidance.
    
    Args:
        error: The exception that occurred
    """
    print("\n" + "=" * 70)
    print("✗ Error Occurred!")
    print("=" * 70)
    print(f"\nError: {error}")
    print("\nTroubleshooting:")
    print("  1. Verify 'temperatures' folder exists in current directory")
    print("  2. Ensure CSV files are present in 'temperatures' folder")
    print("  3. Check CSV format: STATION_NAME, January-December columns")
    print("  4. Verify you have write permissions for 'output' folder")
    print("=" * 70)


def execute_analysis_workflow():
    """
    Execute the complete analysis workflow.
    Separated to enable easier testing and maintenance.
    
    Raises:
        Various exceptions if any step fails
    """
    display_header()
    
    print("[Step 1/5] Loading temperature data...")
    raw_data = load_all_temperature_data()
    
    print("[Step 2/5] Transforming data...")
    long_format_data = transform_to_long_format(raw_data)
    
    print("[Step 3/5] Analyzing seasonal averages...")
    seasonal_averages = calculate_seasonal_averages(long_format_data.copy())
    save_seasonal_averages(seasonal_averages, OUTPUT_SEASONAL_AVG)
    print()
    
    print("[Step 4/5] Finding largest temperature ranges...")
    range_results = find_largest_range_stations(long_format_data.copy())
    save_range_results(range_results, OUTPUT_TEMP_RANGE)
    print()
    
    print("[Step 5/5] Analyzing temperature stability...")
    stable_stations, variable_stations = analyze_temperature_stability(
        long_format_data.copy()
    )
    save_stability_results(stable_stations, variable_stations, OUTPUT_TEMP_STABILITY)
    print()
    
    display_footer()


def main():
    """
    Main execution function with comprehensive error handling.
    """
    try:
        execute_analysis_workflow()
    except FileNotFoundError as e:
        display_error(f"File/Folder not found: {e}")
    except ValueError as e:
        display_error(f"Data validation error: {e}")
    except PermissionError as e:
        display_error(f"Permission error: {e}")
    except OSError as e:
        display_error(f"System error: {e}")
    except Exception as e:
        display_error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()