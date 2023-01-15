import sqlite3

conNect = sqlite3.connect("NagDate.db")
cur = conNect.cursor()

res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

