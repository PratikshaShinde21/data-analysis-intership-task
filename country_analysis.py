
# Task 3: Country-Wise Netflix Content Analysis

# Step 1: Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")


# Step 2: Load Cleaned Dataset

df = pd.read_csv("Netflix_Cleaned.csv")

print("Netflix dataset loaded successfully!")

# Display country column
print(df["country"].head())


# Step 3: Check Missing Country Values

print("Missing Country Values:")
print(df["country"].isnull().sum())

print("\nNot Given Countries:")
print((df["country"] == "Not Given").sum())


# Step 4: Clean Country Data

# Remove extra spaces
df["country"] = df["country"].str.strip()

# Replace Not Given with empty value
df["country"] = df["country"].replace("Not Given", pd.NA)

# Remove rows where country is missing
df = df.dropna(subset=["country"])

print("\nCountry data cleaned successfully!")

print("Remaining missing values:")
print(df["country"].isnull().sum())


# Step 5: Split Country Names

df["country"] = df["country"].str.split(",")

print("Country names split successfully!")

print(df["country"].head())


# Step 6: Explode Country Column

df = df.explode("country")

# Remove extra spaces
df["country"] = df["country"].str.strip()

print("\nCountry data after explode:")
print(df[["title", "country"]].head(10))

# Step 7: Count Content by Country

country_counts = df["country"].value_counts()

print("Top 10 Countries with Most Netflix Content:")
print(country_counts.head(10))

# Step 8: Top 10 Countries Bar Chart

top_10 = country_counts.head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_10.values, y=top_10.index)

plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Number of Movies and TV Shows")
plt.ylabel("Country")
plt.tight_layout()

plt.show()

# Step 9: Create Country Ranking Report

country_ranking = country_counts.reset_index()

country_ranking.columns = ["Country", "Content Count"]

country_ranking["Rank"] = range(1, len(country_ranking) + 1)

country_ranking = country_ranking[["Rank", "Country", "Content Count"]]

print("Country Ranking Report:")
print(country_ranking.head(10))

# Save report as CSV
country_ranking.to_csv("Country_Ranking_Report.csv", index=False)

print("\nCountry ranking report saved successfully!")

# Step 10: Business Insights

print("\nBusiness Insights")

print("Top 5 Countries:")
print(country_counts.head(5))

print("\nCountry with Highest Content:")
print(country_counts.idxmax())

print("\nTotal Countries:")
print(len(country_counts))