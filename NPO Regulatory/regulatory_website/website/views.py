__author__ = 'ammonk'

from flask.views import View, MethodView
from flask import render_template, g, url_for, redirect, flash, request
import website.db.database as datab
from website import app
import json
from content_manager import Content

CONTENT = Content()

#configuration
SECRET_KEY ='monkeysauce'
app.config.from_object(__name__)

@app.before_request
def before_request():
    g.db = datab.database('website/db/website.db')


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

class Dashboard(MethodView):
    def get(self):
        products = g.db.get_products()
        TOC = CONTENT.TOC
        #products = ['bob', 'fred']
        return render_template('dashboard.html', products=products, TOC=TOC)
app.add_url_rule('/', view_func=Dashboard.as_view('dashboard'))

class Products(MethodView):
    def get(self):
        products = g.db.get_products()
        TOC = CONTENT.TOC
        #products = ['bob', 'fred']
        return render_template('products.html', products=products, TOC=TOC)
app.add_url_rule('/products/', view_func=Products.as_view('products'))

class Calendar(MethodView):
    def dispatch_request(self, *args, **kwargs):
        TOC = CONTENT.TOC
        return render_template('calendar.html', TOC=TOC)
app.add_url_rule('/calendar/', view_func=Calendar.as_view('timeline'))

class AddProduct(MethodView):
    def get(self, *args, **kwargs):
        customers = CONTENT.CUSTOMER
        silicon = CONTENT.SILICON
        TOC = CONTENT.TOC
        return json.dumps(dict(customer=customers, silicon=silicon))

    def post(self):
        try:
            attempted_product = request.form['productname']
            customer = request.form['customer']
            attempted_pba = request.form['pba']
            silicon = request.form['silicon']
            notes = request.form['notes']
            ports = request.form['ports']
            if ports == "1":
                ports = "SP"
            elif ports == "2":
                ports = "DP"
            elif ports == "4":
                ports = "QP"
            flash(notes)
        except Exception as e:
            flash(e)
        try:
            g.db.add_product([attempted_product, customer, attempted_pba,
                              ports, silicon, notes])
        except Exception as e:
            flash(e)
        return redirect(url_for('products'))
addProduct_view = AddProduct.as_view('add_product')
app.add_url_rule('/add_product/', view_func=addProduct_view, methods=['GET',])
app.add_url_rule('/add_product/', view_func=addProduct_view, methods=['POST',])

class AddTestplan(MethodView):
    def get(self, *args, **kwargs):
        TOC = CONTENT.TOC
        return render_template('/testplan/add_testplan.html', TOC=TOC)
addTestplan_view = AddTestplan.as_view('add_testplan')
app.add_url_rule('/testplan/add_testplan/', view_func=addTestplan_view, methods=['GET',])

class Product(MethodView):
    def get(self, product):
        TOC = CONTENT.TOC
        pid = request.args.get('pid')
        try:
            details = g.db.get_product(pid)
            name = g.db.product_name(details)
            regulatory = g.db.c.execute("SELECT * FROM regulatory WHERE pid is '%s'" % pid)
            #regulatory = "bob"
        except Exception as e:
            flash(e)
        return render_template('product/product.html', pid=pid, regulatory=regulatory, product=details, TOC=TOC, name=name)
app.add_url_rule('/product/<product>/', view_func=Product.as_view('product'))

class AddRegulatory(MethodView):
    def get(self):
        regulatory = CONTENT.REGULATORY
        TOC = CONTENT.TOC
        pid = request.args.get('pid')
        details = g.db.get_product(pid)
        name = g.db.product_name(details)
        try:
            list = g.db.c.execute("SELECT * FROM regulatory WHERE pid is '%s'" % pid)
        except Exception as e:
            flash(e)
        return render_template('regulatory/add_job.html', name=name, TOC = TOC, pid = pid, regulatory=regulatory, list = list)

    def post(self):
        try:
            jobn = request.form['jobn']
        except Exception as e:
            flash(e)
        return render_template('regulatory/add_job.html')
app.add_url_rule('/product/add_job/', view_func=AddRegulatory.as_view('add_job'))

