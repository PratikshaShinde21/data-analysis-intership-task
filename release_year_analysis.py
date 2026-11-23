import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")

# Step 2: Load Dataset

df = pd.read_csv("Netflix_Cleaned.csv")

print("Dataset loaded successfully!")

print(df[["title", "release_year"]].head(10))

# Step 3: Count Content by Release Year

yearly_content = df["release_year"].value_counts().sort_index()

print("Yearly Netflix Content Releases:")
print(yearly_content)

# Step 4: Identify Growth and Decline Trends

yearly_content = yearly_content.sort_index()

print("First Release Year:", yearly_content.index.min())
print("Latest Release Year:", yearly_content.index.max())

print("\nTop 5 Years with Most Content:")
print(yearly_content.sort_values(ascending=False).head(5))

print("\nYear with Highest Content:")
print(yearly_content.idxmax())

print("Highest Content Count:", yearly_content.max())

# Step 5: Yearly Trend Chart

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=yearly_content.index,
    y=yearly_content.values,
    marker="o"
)

plt.title("Netflix Content Release Trend by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

# Step 6: Business Insights

print("\nNetflix Business Insights")

print("1. Netflix content releases increased over the years.")
print("2. Some years have more content releases than others.")
print("3. The line chart shows changes in yearly content releases.")
print("4. Netflix can study popular release periods to plan future content.")
print("5. Year-wise analysis helps understand historical content trends.")