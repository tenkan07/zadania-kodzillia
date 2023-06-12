# ex_02_create_tables.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   trenerzy_sql = """
   -- trenerzy table
   CREATE TABLE IF NOT EXISTS trenerzy (
      id integer PRIMARY KEY,
      imię text NOT NULL,
      nazwisko text NOT NULL,
      zespół text 
   );
   """

   zawodnicy_sql = """
   -- zawodnicy table
   CREATE TABLE IF NOT EXISTS zawodnicy (
      id integer PRIMARY KEY,
      trener_id integer NOT NULL,
      imię TEXT NOT NULL,
      nazwisko TEXT NOT NULL,
      numer integer NOT NULL,
      pozycja text NOT NULL,
      zespół text NOT NULL,
      FOREIGN KEY (trener_id) REFERENCES projects (id)
   );
   """

   db_file = "database.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, trenerzy_sql)
       execute_sql(conn, zawodnicy_sql)
       conn.close()