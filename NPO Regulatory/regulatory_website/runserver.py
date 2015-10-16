__author__ = 'ammonk'

from website import app

app.run(debug = True)

"""
import website.db.database as datab

if __name__ == "__main__":
    db = datab.database('website/db/regulatory.db')
    r = db.c.execute('''
            SELECT name FROM
            (SELECT * FROM sqlite_master UNION ALL
            SELECT * FROM sqlite_temp_master)
            WHERE type='table'
            ORDER BY name''')
    for row in r:
        print row
"""