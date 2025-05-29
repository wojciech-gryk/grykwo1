import sqlite3

con = sqlite3.connect("baza.db")
cur = con.cursor()

sql_query = """
create table osoba (
    id int not null,
    name varchar(255)
)
"""

cur.execute(sql_query)

sql_query = """
insert into osoba (id, name) values (1, "Jan")
"""

cur.execute(sql_query)
con.commit()