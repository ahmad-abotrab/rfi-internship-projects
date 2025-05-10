import pandas as pd
import random
from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(2000, 1, 1)
end_date = datetime(2025, 12, 31)
delta = end_date - start_date
total_days = delta.days + 1  # Include both start and end dates

# Define different date formats
date_formats = [
    lambda dt: dt.strftime('%Y-%m-%d'),                # 2025-05-01
    lambda dt: f"{dt.year} - {dt.strftime('%b')} - {dt.day}",  # 2025 - May - 1
    lambda dt: dt.strftime('%m/%d/%Y'),                # 05/01/2025
    lambda dt: dt.strftime('%d-%b-%Y').upper(),         # 01-MAY-2025
]

# Read Excel file
file_path = '/Users/ahmad/PyCharmMiscProject/rfi-internship-projects/Task_2/Border_Crossing_Entry_Data.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Ensure DataFrame has exactly 19505 rows
if len(df) < 19505:
    df = df.reindex(range(19505))
elif len(df) > 19505:
    df = df.iloc[:19505]

# Generate random dates with different formats
random_dates = []
for _ in range(19505):
    # Generate random date
    random_day = random.randint(0, total_days - 1)
    date = start_date + timedelta(days=random_day)
    
    # Select random format
    formatter = random.choice(date_formats)
    random_dates.append(formatter(date))

# Add/update column with generated dates
df['Random Dates'] = random_dates

# Save back to Excel file
df.to_excel(file_path, index=False)

print("Excel file updated successfully with random dates!")