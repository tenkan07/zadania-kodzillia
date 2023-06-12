import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

conn = create_connection("database.db")

cur = conn.cursor()
cur.execute("SELECT * FROM zawodnicy")
rows = cur.fetchall()
#print(rows)

def select_all(conn, table):
   
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

print(select_all(conn, "trenerzy"))
print(select_where(conn, "zawodnicy", trener_id=1))