import sqlite3

con = sqlite3.connect("baza.db")
cur = con.cursor()

osoby = [
    (20, "Adam"),
    (21, "DDDDD"),
    (22, "Piotr")
]

sql = f"""
insert into osoba (id, name) values (?, ?)
"""

cur.executemany(sql, osoby)
con.commit()