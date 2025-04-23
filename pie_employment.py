import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("D:/project/1/survey_data.db")

# Query to get the count of each employment type
df = pd.read_sql_query("SELECT Employment, COUNT(*) as Count FROM survey WHERE Employment IS NOT NULL GROUP BY Employment", conn)

# Sort the data by count in descending order and limit to the top 5
df_sorted = df.sort_values(by='Count', ascending=False)

# Set the threshold for top categories (top 5)
top_n = 5

# If there are more than 5 categories, combine the rest into 'Other'
if len(df_sorted) > top_n:
    other_count = df_sorted.iloc[top_n:]['Count'].sum()
    df_sorted = df_sorted.iloc[:top_n]  # Keep only the top N categories
    other_df = pd.DataFrame([['Other', other_count]], columns=['Employment', 'Count'])
    df_sorted = pd.concat([df_sorted, other_df], ignore_index=True)

# Plotting the pie chart
plt.figure(figsize=(8, 8))  # Increase figure size for better clarity
colors = plt.cm.Paired.colors  # A color palette with distinct colors
plt.pie(df_sorted['Count'], labels=df_sorted['Employment'], autopct='%1.1f%%', startangle=140, colors=colors[:len(df_sorted)])
plt.title('Top Employment Type Distribution (with Other)')

# Equal aspect ratio ensures that pie chart is drawn as a circle.
plt.axis('equal')

# Add a legend for the employment types
plt.legend(df_sorted['Employment'], loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to prevent overlap and make it more readable
plt.tight_layout()

# Show the plot
plt.show()

# Close the database connection
conn.close()
