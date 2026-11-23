# Task 2: Content Type Analysis Dashboard

# Step 1: Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("All libraries imported successfully!")


# Step 2: Load Cleaned Dataset

df = pd.read_csv("Netflix_Cleaned.csv")

print("Netflix dataset loaded successfully!")

# Display first 5 records
print(df.head())


# Step 3: Calculate Content Types

content_counts = df["type"].value_counts()

print("\nNetflix Content Distribution:")
print(content_counts)

# Calculate total Movies
total_movies = content_counts.get("Movie", 0)

# Calculate total TV Shows
total_tv_shows = content_counts.get("TV Show", 0)

print("\nTotal Movies:", total_movies)
print("Total TV Shows:", total_tv_shows)



# Step 4: Calculate Content Percentage

total_content = len(df)

movie_percentage = (total_movies / total_content) * 100
tv_percentage = (total_tv_shows / total_content) * 100

print("\nContent Percentage:")
print("Movies:", round(movie_percentage, 2), "%")
print("TV Shows:", round(tv_percentage, 2), "%")



# Step 5: Bar Chart using Matplotlib

plt.figure(figsize=(8, 5))

plt.bar(
    content_counts.index,
    content_counts.values
)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.show()


# Step 6: Pie Chart using Matplotlib

plt.figure(figsize=(7, 7))

plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Netflix Content Distribution")

plt.show()



# Step 7: Seaborn Count Plot

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Content Type Analysis")
plt.xlabel("Content Type")
plt.ylabel("Total Count")

plt.show()


# Step 8: Key Findings

print("\n-------- NETFLIX CONTENT ANALYSIS ---------")

print("Total Content:", total_content)

print("Total Movies:", total_movies)
print("Total TV Shows:", total_tv_shows)

print("Movie Percentage:", round(movie_percentage, 2), "%")
print("TV Show Percentage:", round(tv_percentage, 2), "%")

if movie_percentage > tv_percentage:
    print("Finding: Movies are more available than TV Shows on Netflix.")
else:
    print("Finding: TV Shows are more available than Movies on Netflix.")

print("-----------------------------------------------")

