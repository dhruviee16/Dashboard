import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("D:/project/1/survey_data.db")

# Query: average WorkExp per country
df = pd.read_sql_query("""
SELECT Country, AVG(WorkExp) as AvgWorkExp
FROM survey
WHERE Country IS NOT NULL AND WorkExp IS NOT NULL
GROUP BY Country
ORDER BY AvgWorkExp DESC
LIMIT 15
""", conn)

# Plot
plt.figure(figsize=(12,6))
plt.plot(df['Country'], df['AvgWorkExp'], marker='o', linestyle='-', color='purple')
plt.title('Average Work Experience by Country')
plt.xlabel('Country')
plt.ylabel('Avg Work Experience (Years)')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.show()

conn.close()
