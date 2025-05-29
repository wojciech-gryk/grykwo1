import sqlite3

con = sqlite3.connect("baza.db")
cur = con.cursor()

name = input("podaj imię: ")

# ŹŁE !!!!!!!!!!!!!!!!!!
#sql = f"""
#insert into osoba (id, name) values (10, '{name}')
#"""

# DOBRZE
sql = f"""
insert into osoba (id, name) values (10, ?)
"""


cur.execute(sql, (name,))    # tu dochodzi parametr (name,)
con.commit()rrrrr