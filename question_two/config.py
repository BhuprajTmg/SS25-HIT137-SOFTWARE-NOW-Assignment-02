# Directory paths
TEMPERATURES_FOLDER = "temperatures"
OUTPUT_FOLDER = "output"

# Output file paths
OUTPUT_SEASONAL_AVG = "output/average_temp.txt"
OUTPUT_TEMP_RANGE = "output/largest_temp_range_station.txt"
OUTPUT_TEMP_STABILITY = "output/temperature_stability_stations.txt"

# Season mapping for Australian climate zones
# Southern hemisphere seasons differ from northern hemisphere
SEASON_MAPPING = {
    'January': 'Summer',
    'February': 'Summer',
    'March': 'Autumn',
    'April': 'Autumn',
    'May': 'Autumn',
    'June': 'Winter',
    'July': 'Winter',
    'August': 'Winter',
    'September': 'Spring',
    'October': 'Spring',
    'November': 'Spring',
    'December': 'Summer'
}

# Expected month columns in CSV files
MONTH_COLUMNS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Output order for consistent reporting
SEASON_ORDER = ['Summer', 'Autumn', 'Winter', 'Spring']

# Possible station identifier column names for flexibility
STATION_COLUMN_NAMES = ['STATION_NAME', 'Station', 'STN_ID', 'station_name', 'StationName']

# Decimal precision for output formatting
OUTPUT_PRECISION = 1