import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Correct database path to absolute one
conn = sqlite3.connect('D:/project/1/survey_data.db')

# Read the language column
df = pd.read_sql_query("""
SELECT LanguageHaveWorkedWith
FROM survey
WHERE LanguageHaveWorkedWith IS NOT NULL
""", conn)

# Split multiple languages and count
all_languages = df['LanguageHaveWorkedWith'].str.split(';').explode()
language_counts = Counter(all_languages)

# Create a dataframe from the counter
lang_df = pd.DataFrame(language_counts.items(), columns=['Language', 'Count'])
lang_df = lang_df.sort_values(by='Count', ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.bar(lang_df['Language'], lang_df['Count'], color='blue')
plt.title('Top 10 Programming Languages Used')
plt.xlabel('Language')
plt.ylabel('Number of Developers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()
