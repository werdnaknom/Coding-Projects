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

    def init_db(self):
        with open("schema.sql", "r") as f:
            self.c.executescript(f.read())
        self.conn.commit()

    def add_product(self, values):
        name, customer, pba, ports, silicon, notes = values
        status = "Need Test Plan"
        self.c.execute('''insert into products(name, customer, pba, ports, silicon, status, notes)
                values(?, ?, ?, ?, ?, ?, ?)''', [name, customer, pba, ports,
                                                 silicon, status, notes])
        self.conn.commit()

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
    try:

        db = database('website.db')
        db.init_db()

    except:
        raise