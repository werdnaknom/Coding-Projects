__author__ = 'ammonk'

from flask.views import View, MethodView
from flask import render_template, g
import website.db.database as datab
from website import app

@app.before_request
def before_request():
    g.db = datab.database('website/db/regulatory.db')


#@app.teardown_request
#def teardown_request(exception):
#    db = getattr(g, 'db', None)
#    if db is not None:
#        db.close()

class Homepage(MethodView):

    def get(self):
        products = g.db.c.execute("SELECT * from Products")
        #products = ['bob', 'fred']
        return render_template('home.html', products=products)

app.add_url_rule('/', view_func=Homepage.as_view('homepage'))

class Users(MethodView):

    def get(self, user):
        users = user
        return render_template('user.html', users=user)

app.add_url_rule('/<user>', view_func=Users.as_view('users'))
