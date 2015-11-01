__author__ = 'Stratadon'

import sqlite3, time

class database():

    def __init__(self, db):
        self.tables = {"products" : "products",
                       "regulatory" : "regulatory",
                       }
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
    db = database('website.db')
    p = db.c.execute("SELECT * FROM products")
    for prod in p:
        print prod
    #db.c.execute("INSERT INTO regulatory(pid) VALUES('4')")
    #db.conn.commit()
    #r = db.c.execute("SELECT * FROM regulatory")
    reg = db.c.execute("SELECT * FROM regulatory")
    for prod in reg:
        print prod
    try:
        '''
        db = database('website.db')
        db.init_db()
        '''

    except:
        raise