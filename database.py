import sqlite3

conn = sqlite3.connect('matrix.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS eisenhower(
          id_task INTEGER PRIMARY KEY AUTOINCREMENT,
          task TEXT,
          description TEXT,
          status TEXT,
          date TEXT
          );
          ''')

conn.commit()
conn.close()
