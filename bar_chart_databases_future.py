import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
print("📥 Loading dataset...")
df = pd.read_csv('data/final_cleaned_data.csv')
print("✅ Data loaded")

# Split the 'DatabaseWantToWorkWith' column by ';' and count frequencies
print("🔄 Processing DatabaseWantToWorkWith...")
want_db_series = df['DatabaseWantToWorkWith'].dropna().str.split(';')
want_db_flat = [db.strip() for sublist in want_db_series for db in sublist]
want_db_counts = pd.Series(want_db_flat).value_counts().head(10)

# Plotting
plt.figure(figsize=(10, 6))
want_db_counts.plot(kind='bar', color='lightgreen')
plt.title('Top 10 Databases Developers Want to Work With')
plt.xlabel('Database')
plt.ylabel('Number of Developers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('top_10_desired_databases_barchart.png')
plt.show()
