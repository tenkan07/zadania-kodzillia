# ex_03.py
import sqlite3

def create_connection(db_file):
   
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_trener(conn, trener):
   
   sql = '''INSERT INTO trenerzy(imię, nazwisko, zespół)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, trener)
   conn.commit()
   return cur.lastrowid

def add_zawodnik(conn, zawodnik):
  
   sql = '''INSERT INTO zawodnicy(trener_id, imię, nazwisko, numer, pozycja, zespół)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, zawodnik)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   trener = ("Jacek", "Magiera", "Śląsk Wrocław")

   conn = create_connection("database.db")
   trener_id = add_trener(conn, trener)

   zawodnik01 = (
       trener_id,
       "Eric",
       "Expósito",
       "9",
       "napastnik",
       "Śląsk Wrocław"
   )
   zawodnik02 = (
       trener_id,
       "John",
       "Yeboah",
       "7",
       "napastnik",
       "Śląsk Wrocław"
   )
   zawodnik03 = (
       trener_id,
       "Petr",
       "Schwarz",
       "17",
       "Pomocnik",
       "Śląsk Wrocław"
   )

   zawodnik_id = add_zawodnik(conn, zawodnik01)
   add_zawodnik(conn, zawodnik02)
   add_zawodnik(conn, zawodnik03)

   print(trener_id, zawodnik_id)
   conn.commit()