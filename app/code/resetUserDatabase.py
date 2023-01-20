### Code to reset user database
import sqlite3
con = sqlite3.connect('../../app/db.sqlite')
cur = con.cursor()
cur.execute("DROP TABLE user")
cur.execute("CREATE TABLE user(id, email, password, name)")
