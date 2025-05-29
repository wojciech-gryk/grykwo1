import sqlite3

con = sqlite3.connect("baza.db")
cur = con.cursor()

sql_query = """
select name from osoba
"""

res= cur.execute(sql_query)
data = res.fetchall()
for osoba in data:
    print(f"Imię: {osoba[0]}")