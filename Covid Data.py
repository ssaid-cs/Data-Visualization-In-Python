import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("NYC Covid Data/NYC Covid Info.csv")


df['date_of_interest'] = pd.to_datetime(df['date_of_interest'], format='%m/%d/%Y', errors='coerce')

df_clean = df.dropna(subset=['DEATH_COUNT', 'date_of_interest', 'HOSPITALIZED_COUNT'])

# Get the years
df_clean['year'] = df_clean['date_of_interest'].dt.year

# Aggregate death counts and hospitalization by year
deaths_by_year = df_clean.groupby('year')['DEATH_COUNT'].sum().reset_index()
hos_by_year = df_clean.groupby('year')['HOSPITALIZED_COUNT'].sum().reset_index()

#Summary
print("\n\n\nSummary of first 30 Death Counts:")
print(df_clean['DEATH_COUNT'].head(31))

# Plotting
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(data=deaths_by_year, x='year', y='DEATH_COUNT', palette='Reds')

plt.title("NYC Covid Death Count")
plt.ylabel("Death Count")
plt.xlabel("Year")
plt.tight_layout()
plt.show()

# Second Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=hos_by_year, x='year', y='HOSPITALIZED_COUNT', palette='Reds')

plt.title("NYC Covid Hospitalized Count")
plt.ylabel("Hospitalization Count")
plt.xlabel("Year")
plt.tight_layout()
plt.show()