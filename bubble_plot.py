# visualization/bubble_plot_distribution.py

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("D:/project/1/survey_data.db")

# Query
df = pd.read_sql_query("""
SELECT Age, WorkExp, TimeSearching 
FROM survey 
WHERE Age IS NOT NULL AND WorkExp IS NOT NULL AND TimeSearching IS NOT NULL
""", conn)

# Mapping TimeSearching text to numeric values
time_mapping = {
    "Less than 15 minutes a day": 1,
    "15-30 minutes a day": 2,
    "30-60 minutes a day": 3,
    "60-120 minutes a day": 4,
    "Over 120 minutes a day": 5
}
df["TimeSearchingNum"] = df["TimeSearching"].map(time_mapping)
df = df.dropna(subset=["TimeSearchingNum"])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Age"], df["WorkExp"], s=df["TimeSearchingNum"] * 30, alpha=0.5, color="teal")
plt.title("Bubble Plot: Age vs Work Experience (Size = Time Spent Searching)")
plt.xlabel("Age")
plt.ylabel("Work Experience")
plt.grid(True)
plt.tight_layout()
plt.show()

conn.close()
