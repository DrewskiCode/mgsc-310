import pandas as pd

# Load the dataset
file_path = "uber_data_bookings.csv"  # Ensure the file name matches exactly

# Add error handling for other potential issues
try:
    uber_data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file name and its location.")
    exit()
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
    exit()
except pd.errors.ParserError:
    print(f"Error: The file '{file_path}' could not be parsed. Please check if it is a valid CSV file.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Print the first 10 rows
print("=" * 50)
print("First 10 rows of the dataset:")
print(uber_data.head(10))
print("=" * 50)

# Display column names
print("\nColumn Names:")
print("-" * 50)
print(uber_data.columns.to_list())
print("-" * 50)

# Display basic information about the dataset
print("\nDataset Info:")
print("-" * 50)
uber_data.info()
print("-" * 50)

# Display summary statistics
print("\nSummary Statistics:")
print("-" * 50)
print(uber_data.describe())
print("-" * 50)

# Inspect column names
print("\nInspecting Column Names:")
print("-" * 50)
print(uber_data.columns.to_list())
print("-" * 50)

# Data Cleaning Functions
def clean_column(column):
    """Generic cleaning function for string columns."""
    return column.str.strip() if column.dtype == "object" else column

# Apply cleaning to all columns
uber_data = uber_data.apply(clean_column)

# Check for null values
print("\nNull Value Analysis:")
print("-" * 50)
print(uber_data.isnull().sum())
print("-" * 50)

# Recommend handling null values
null_threshold = 0.3  # Drop columns with more than 30% null values
columns_to_drop = uber_data.columns[uber_data.isnull().mean() > null_threshold]
if not columns_to_drop.empty:
    print(f"\nDropping columns with more than {null_threshold * 100}% null values: {columns_to_drop.tolist()}")
    uber_data = uber_data.drop(columns=columns_to_drop)

# Drop rows with any remaining null values
print("\nDropping rows with remaining null values...")
uber_data = uber_data.dropna()

# Check for null values
print("\nNull Value Analysis:")
print("-" * 50)
print(uber_data.isnull().sum())
print("-" * 50)

# Display cleaned dataset
print("\nCleaned Dataset:")
print("-" * 50)
print(uber_data.head(10))
print("-" * 50)

