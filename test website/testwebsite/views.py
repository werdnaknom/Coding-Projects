# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from contextlib import closing
from flask.views import View, MethodView
from testwebsite import app

'''
class ShowUsers(View):
    def dispatch_request(self):
        users = User.query.all()
        return render_template('users.html', objects=users)

app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))
'''

# configuration
DATABASE = 'tmp/regulatory.db'
DEBUG = True
Testing = False
SECRET_KEY = 'monkeysauce'
USERNAME = 'admin'
PASSWORD = 'default'

users = ["bob", "fred", "Josh"]

class HomePage(View):
    def dispatch_request(self):
        return render_template('homepage.html', users=users)

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

def home_page():
    return "hello world"

class BlockTemplate(View):
    def dispatch_request(self):
        return render_template('child_template.html')
app.add_url_rule('/template/', view_func=BlockTemplate.as_view(('block_template')))

class UserAPI(MethodView):
    def get(self):
        users = ["bob", "bobby", "bobbett"]
        return users

    def post(self):
        return redirect(url_for('homepage'))

    def dispatch_request(self):
       return render_template('users.html', users=users)

app.add_url_rule('/users/',  view_func=UserAPI.as_view('users'))

'''
# Create flaskr application
app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    g.db=connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with closing(connect_db()) as db:  # keeps connection open for duration of the with block
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=["POST"])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
'''