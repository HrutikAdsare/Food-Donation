import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


cursor.execute("SELECT * from donates")
rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()
