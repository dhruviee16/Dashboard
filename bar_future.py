import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Correct database path to absolute one
conn = sqlite3.connect('D:/project/1/survey_data.db')

# Read the language column for languages they want to work with
df_want = pd.read_sql_query("""
SELECT LanguageWantToWorkWith
FROM survey
WHERE LanguageWantToWorkWith IS NOT NULL
""", conn)

# Split multiple languages and count
all_languages_want = df_want['LanguageWantToWorkWith'].str.split(';').explode()
language_counts_want = Counter(all_languages_want)

# Create a dataframe from the counter
lang_df_want = pd.DataFrame(language_counts_want.items(), columns=['Language', 'Count'])
lang_df_want = lang_df_want.sort_values(by='Count', ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.bar(lang_df_want['Language'], lang_df_want['Count'], color='orange')
plt.title('Top 10 Programming Languages Developers Want to Work With')
plt.xlabel('Language')
plt.ylabel('Number of Developers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()
