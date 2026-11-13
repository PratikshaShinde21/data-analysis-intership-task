
# Step 1: Import Libraries

import pandas as pd

print("Pandas imported successfully!")

# Step 2: Import Netflix Dataset
df = pd.read_csv("Dataset.csv")

print("Dataset imported successfully!")

# Display first 5 rows
print(df.head())

# Step 3: Explore Dataset

# Check total rows and columns
print("Dataset Shape:")
print(df.shape)

# Check column names
print("\nColumn Names:")
print(df.columns)

# Check dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Handle Missing Values

# Check missing values before cleaning
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing text values
df = df.fillna("Not Given")

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 5: Remove Duplicate Records

# Check duplicate records
print("Duplicate records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Check duplicates after cleaning
print("\nDuplicates after cleaning:")
print(df.duplicated().sum())


# Step 6: Standardize Columns

# Standardize Type column
df["type"] = df["type"].str.strip().str.title()

# Standardize Rating column
df["rating"] = df["rating"].str.strip().str.upper()

# Standardize Country column
df["country"] = df["country"].str.strip().str.title()

print("Columns standardized successfully!")

# Display standardized columns
print(df[["type", "rating", "country"]].head())


# Correct TV Show formatting
df["type"] = df["type"].replace({
    "Tv Show": "TV Show"
})

print(df["type"].value_counts())



# Step 7: Date Formatting

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Convert date into YYYY-MM-DD format
df["date_added"] = df["date_added"].dt.strftime("%Y-%m-%d")

# Handle missing dates
df["date_added"] = df["date_added"].fillna("Not Given")

print("Date formatting completed!")
print(df["date_added"].head())

# Step 8: Export Cleaned Dataset

df.to_csv("Netflix_Cleaned.csv", index=False)

print("Cleaned dataset exported successfully!")

# Final dataset information
print("Final Dataset Shape:", df.shape)

print("Total Missing Values:", df.isnull().sum().sum())

print("Total Duplicate Records:", df.duplicated().sum())