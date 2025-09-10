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
null_threshold = 0.7  # Drop columns with more than 30% null values
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

# Display the number of rows in the cleaned dataset
print("\nNumber of rows in the cleaned dataset:")
print("-" * 50)
print(len(uber_data))
print("-" * 50)

# Example Analysis: Distribution of Trip Durations
import matplotlib.pyplot as plt

# Example Analysis: Distribution of Vehicle Types
# Check if the 'Vehicle Type' column exists
if 'Vehicle Type' in uber_data.columns:
    plt.figure(figsize=(10, 6))
    vehicle_counts = uber_data['Vehicle Type'].value_counts()
    total = vehicle_counts.sum()
    ax = vehicle_counts.plot(kind='bar', color='orange', edgecolor='black')
    
    # Add percentages on top of each bar
    for p in ax.patches:
        percentage = f"{(p.get_height() / total) * 100:.1f}%"
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2, p.get_height()), 
                    ha='center', va='bottom', fontsize=10, color='black')
    
    plt.title('Distribution of Vehicle Types', fontsize=16)
    plt.xlabel('Vehicle Type', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("The column 'Vehicle Type' does not exist in the dataset.")

# Example Analysis: Average Trip Duration by Vehicle Type
if 'Vehicle Type' in uber_data.columns and 'Booking Value' in uber_data.columns:
    avg_trip_duration = uber_data.groupby('Vehicle Type')['Booking Value'].mean()
    print("\nAverage Booking Value by Vehicle Type:")
    print(avg_trip_duration)
    
    # Visualize the average trip duration
    plt.figure(figsize=(10, 6))
    avg_trip_duration.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Booking Value by Vehicle Type', fontsize=16)
    plt.xlabel('Vehicle Type', fontsize=12)
    plt.ylabel('Average Booking Value (dollars)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("The required columns 'Vehicle Type' or 'Trip Duration' do not exist in the dataset.")

