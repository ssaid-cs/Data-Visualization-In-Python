import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("NYC Covid Data/NYC Covid Info.csv")
df.info()

df['date_of_interest'] = pd.to_datetime(df['date_of_interest'], format= '%m%d%Y', errors='coerce')

#dropping null values

df.drop(columns=[
    'PROBABLE_CASE_COUNT', 'HOSPITALIZED_COUNT', 'ALL_CASE_COUNT_7DAY_AVG', 'HOSP_COUNT_7DAY_AVG', 'BX_CASE_COUNT'
], inplace=True)

df_clean = df.dropna(subset=['DEATH_COUNT', 'DEATH_COUNT_7DAY_AVG'])

#data analysis

print("\n\n\nSummary of Death distribution:")
print(df_clean['DEATH_COUNT'].value_counts())

deaths_by_year = df_clean.groupby('year')['DEATH_COUNT'].sum().reset_index()


#data visualization 

sns.set_style(style="whitegrid")

#death distribution
death_stats = df_clean['DEATH_COUNT']
date = df_clean['date_of_interest']
plt.figure(figsize=(8,4))

sns.barplot(x=date, y=death_stats)
plt.title("Death Counts")
plt.ylabel("Number of deaths")
plt.xlabel("Dates")
plt.xticks(rotation=45)
plt.show()
