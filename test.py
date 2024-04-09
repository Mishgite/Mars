import sqlite3


con = sqlite3.connect("db/database.db")
cur = con.cursor()
result = cur.execute("""SELECT id FROM jobs""").fetchall()
print(result[-1][-1])