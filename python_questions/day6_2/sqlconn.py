import sqlite3
connection=sqlite3.connect("students.db")
cursor=connection.cursor()
cursor.execute(""" create table if not exists students(id integer, name text)""")
connection.commit()
connection.close()