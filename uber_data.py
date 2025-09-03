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