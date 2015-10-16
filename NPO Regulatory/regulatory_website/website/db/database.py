__author__ = 'Stratadon'

import sqlite3, time

class database():
    def __init__(self, db):
        self.tables = {"products" : "products"}
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def _sanitize(self, tablename):
        try:
            return self.tables[tablename.lower()]
        except KeyError, e:
            return e

    def create_table(self, table, sql):
        try:
            self.c.execute(sql)
            self.conn.commit()
        except:
            print "CREATE"
            self.conn.rollback()

    def select(self, s=None):
        if s == None:
            s = "*"
        try:
            statement = "SELECT %s FROM regulatory" % s
            print statement
            self.c.execute("SELECT * from regulatory")
        except:
            print "SELECT"


    def insert(self, s):
        print s
        try:
            self.c.execute("INSERT INTO regulatory VALUES (%s, %s )" % (s, time.strftime("%m/%d/%Y")))
            self.conn.commit()
        except:
            print "INSERT"
            self.conn.rollback()

if __name__ == "__main__":
    import sqlite3 as lite
    import sys
    print hello
    try:

        db = database('regulatory.db')

        sql = ''' CREATE TABLE IF NOT EXISTS Products (SUBID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT, CUSTOMER TEXT, PBA TEXT, DATECOL DATE, NOTES TEXT)'''
        db.c.execute(sql)
        db.c.execute("""INSERT INTO Products(NAME, CUSTOMER, PBA, DATECOL, NOTES)
                     VALUES('Spirit Falls', 'HP', 'H12345-001', DATE('NOW'), 'test test test')""" )
        db.conn.commit()
        rows = db.c.execute("SELECT * FROM Products")
        for row in rows:
            print row
    except:
        raise