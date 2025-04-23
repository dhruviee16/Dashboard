import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("D:/project/1/survey_data.db")

# Query to get counts of employment types by country
df = pd.read_sql_query("""
SELECT Country, Employment, COUNT(*) as Count
FROM survey
WHERE Country IS NOT NULL AND Employment IS NOT NULL
GROUP BY Country, Employment
""", conn)

conn.close()

# Pivot the data for a stacked bar chart
pivot_df = df.pivot(index='Country', columns='Employment', values='Count').fillna(0)

# Sort by total counts and pick top 10 countries
pivot_df['Total'] = pivot_df.sum(axis=1)
pivot_df = pivot_df.sort_values(by='Total', ascending=False).head(10)
pivot_df = pivot_df.drop(columns='Total')

# Plot
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(12, 7), colormap='tab20c')
plt.title('Employment Types by Country (Top 10 Countries)')
plt.xlabel('Country')
plt.ylabel('Number of Developers')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Move the legend outside the plot
plt.legend(title='Employment Type', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

# Adjust layout
plt.subplots_adjust(right=0.75)

plt.show()


# Query to get counts of employment types by country
df = pd.read_sql_query("""
SELECT Country, Employment, COUNT(*) as Count
FROM survey
WHERE Country IS NOT NULL AND Employment IS NOT NULL
GROUP BY Country, Employment
""", conn)

conn.close()

# Pivot the data for a stacked bar chart
pivot_df = df.pivot(index='Country', columns='Employment', values='Count').fillna(0)

# Sort by total counts and pick top 10 countries
pivot_df['Total'] = pivot_df.sum(axis=1)
pivot_df = pivot_df.sort_values(by='Total', ascending=False).head(10)
pivot_df = pivot_df.drop(columns='Total')

# Plot
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(12, 7), colormap='tab20c')
plt.title('Employment Types by Country (Top 10 Countries)')
plt.xlabel('Country')
plt.ylabel('Number of Developers')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Move the legend outside the plot
plt.legend(title='Employment Type', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

# Adjust layout
plt.subplots_adjust(right=0.75)

plt.show()
