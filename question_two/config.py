# Folder paths
TEMPERATURES_FOLDER = "temperatures"
OUTPUT_FOLDER = "output"

# Output file names
OUTPUT_SEASONAL_AVG = "output/average_temp.txt"
OUTPUT_TEMP_RANGE = "output/largest_temp_range_station.txt"
OUTPUT_TEMP_STABILITY = "output/temperature_stability_stations.txt"

# Australian Seasons Definition
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

# Month columns expected in CSV files
MONTH_COLUMNS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Season order for output
SEASON_ORDER = ['Summer', 'Autumn', 'Winter', 'Spring']