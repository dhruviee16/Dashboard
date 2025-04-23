import pandas as pd
import sqlite3

# Load the cleaned CSV (final_cleaned_data.csv)
df = pd.read_csv("D:/project/1/final_cleaned_data.csv")

# Create connection to the SQLite database
conn = sqlite3.connect("survey_data.db")

# Save the cleaned data to the table (replace the existing table with new data)
df.to_sql("survey", conn, if_exists="replace", index=False)

# Close the connection
conn.close()

print("Database created and data loaded!")
