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
print("First 10 rows of the dataset:")
print(uber_data.head(10))

# Display column names
print("\nColumn names:")
print(uber_data.columns)

# Display basic information about the dataset
print("\nDataset info:")
print(uber_data.info())

# Display summary statistics
print("\nSummary statistics:")
print(uber_data.describe())