import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Fetch data from a specific table
cursor.execute("SELECT * from donations")
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
