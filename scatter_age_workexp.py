import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("D:/project/1/survey_data.db")

# Read data
df = pd.read_sql_query("SELECT Age, WorkExp FROM survey WHERE Age IS NOT NULL AND WorkExp IS NOT NULL", conn)

# Set a color palette for the plot
sns.set_palette("viridis")

# Create scatter plot with enhancements
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Age', y='WorkExp', alpha=0.6, hue='Age', palette="viridis", edgecolor='w', s=100)

# Add titles and labels
plt.title('Age vs Work Experience', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Work Experience', fontsize=12)

# Grid and layout adjustments
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()

# Close the database connection
conn.close()
