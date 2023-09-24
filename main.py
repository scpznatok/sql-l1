import sqlite3

conn = sqlite3.connect("db.db")

cursor = conn.cursor()
score = 9
cursor.execute('''SELECT * FROM students WHERE avg_score> (?) ''', [score])

data = cursor.fetchall()

for i in range(0, len(data)):
    print(data[i])

conn.commit()


