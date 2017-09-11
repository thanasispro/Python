import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY,title text,director text,year integer,grade  integer )")
        self.conn.commit()


    def insert(self,title,director,year,grade):
        self.cur.execute("INSERT INTO movie VALUES(NULL,?,?,?,?)",(title,director,year,grade))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM movie")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",director="",year="",grade=""):
        self.cur.execute("SELECT * FROM movie WHERE title=? OR director=? OR year=? OR grade=?",(title,director,year,grade))
        rows=self.cur.fetchall()
        return rows



    def delete(self,id):
        self.cur.execute("DELETE FROM movie WHERE id=?",(id,))
        self.conn.commit()



    def update(self,id,title,director,year,grade):
        self.cur.execute("UPDATE movie SET title=?,director=?,year=?,grade=? WHERE id=?",(title,director,year,grade,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
