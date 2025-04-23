import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
print("📥 Loading dataset...")
df = pd.read_csv('data/final_cleaned_data.csv')
print("✅ Data loaded")

# Split the 'DatabaseHaveWorkedWith' column by ';' and count frequencies
print("🔄 Processing DatabaseHaveWorkedWith...")
db_series = df['DatabaseHaveWorkedWith'].dropna().str.split(';')
db_flat = [db.strip() for sublist in db_series for db in sublist]
db_counts = pd.Series(db_flat).value_counts().head(10)

# Plotting
plt.figure(figsize=(10, 6))
db_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Databases Used by Developers')
plt.xlabel('Database')
plt.ylabel('Number of Developers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('top_10_databases_barchart.png')
plt.show()
