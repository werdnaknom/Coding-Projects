__author__ = 'Stratadon'

import sqlite3, time

class database():

    def __init__(self, db):
        self.tables = {"products" : "products",
                       "regulatory" : "regulatory",
                       }
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def close(self):
        self.conn.close()

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

    def get_products(self):
        products = self.c.execute(''' SELECT * FROM products ''')
        return products

    def get_product(self, pid):
        product = dict()
        try:
            details = self.c.execute("SELECT * FROM products WHERE pid is '%s'" % pid)
            for i, item in enumerate(details.fetchone()):
               product[details.description[i][0]] = item
        except Exception as e:
            print e
        return product

    def product_name(self, product):
        name = "%s %s %s" % (product['name'], product['ports'], product['customer'])
        return name


if __name__ == "__main__":
    import sqlite3 as lite
    import sys
    db = database('website.db')

    products = db.get_products()
    #for prod in products:
    #    print prod

    product = db.get_product("1")
    #for item in product:
    #    print item
    print product

    name = db.product_name(product)
    print name
    """
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
    """