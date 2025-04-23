import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
conn = sqlite3.connect("D:/project/1/survey_data.db")

# Query the data
df = pd.read_sql_query("SELECT CompTotal FROM survey WHERE CompTotal IS NOT NULL", conn)

# Plot histogram with KDE
sns.histplot(df["CompTotal"], bins=30, kde=True, color="skyblue")
plt.title("Distribution of Total Compensation")
plt.xlabel("CompTotal")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Close the connection
conn.close()
