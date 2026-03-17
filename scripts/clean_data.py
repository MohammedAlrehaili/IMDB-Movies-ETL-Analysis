import pandas as pd
import numpy as np
import os

# --- PATH CONFIGURATION ---
# Define the script's directory to ensure relative paths work on any machine
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths for input and output files
input_path = os.path.abspath(os.path.join(base_dir, '..','data','imdb_top_1000.csv'))
output_path = os.path.abspath(os.path.join(base_dir, '..', 'data','Cleandimdb_top_1000.csv'))

print(f"🔍 Searching for file at: {input_path}")

# --- DATA LOADING STAGE ---
try:
    if os.path.exists(input_path):
        # Load the dataset and store the initial count for later comparison
        df = pd.read_csv(input_path)
        total_before = len(df)
        print("✅ File found successfully! Starting the cleaning process...")
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("❌ Error: File not found.")
    exit()

# --- CORE CLEANING STAGE ---

# 1. Drop columns that are not relevant for current analysis to save memory
df = df.drop(['Poster_Link','Certificate','Gross'], axis = 1)

# 2. Clean 'Released_Year' column:
# Convert to numeric, turn non-numeric values (like 'PG') into NaN, then drop them
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df.dropna(subset=['Released_Year'], inplace=True)
df['Released_Year'] = df['Released_Year'].astype(int)

# 3. Clean 'Runtime' column:
# Remove the ' min' string suffix and convert the remaining value to integer
df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

# 4. Handle Missing Values in 'Meta_score':
# Fill NaN values with the mean score to maintain dataset size without losing rows
df['Meta_score'] = df['Meta_score'].fillna(df['Meta_score'].mean())

# 5. Text Normalization:
# Strip leading/trailing whitespace from string columns to avoid matching errors
df['Series_Title'] = df['Series_Title'].str.strip()
df['Genre'] = df['Genre'].str.strip()

# 6. Deduplication:
# Remove duplicate entries based on Title and Year to ensure data integrity
df.drop_duplicates(subset=['Series_Title', 'Released_Year'], inplace=True)

# --- RESULTS & EXPORT ---

# Display the updated data types and a preview of the cleaned data
print("---Data Types after Cleaning---")
print(df.dtypes)
print("---First 10 Rows--")
print(df.head(10))

# Export the cleaned DataFrame to a new CSV file (without the index column)
df.to_csv(output_path, index=False)

print("---")
print("✅ Data Cleaning Completed Successfully!")
print(f"📊 Total records before cleaning: {total_before}")
print(f"📊 Total records after cleaning:  {len(df)}")
print(f"📂 Cleaned file saved to: {output_path}")