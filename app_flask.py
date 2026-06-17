from flask import Flask,render_template
from pathlib import Path
from customer_dao import CustomerDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/old")
def oldindex():
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)
    customers = dao.find_all()
    
    html="<ul>"
    for customer in customers:
        html+=f"<li>{customer.first_name},{customer.last_name}</li>"

    html+="</ul>"
    return html

@app.route("/")
def index():
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)
    all_customers = dao.find_all()
    return render_template("customers.html",name="fred",customers=all_customers)

@app.route("/api")
def api():
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)
    all_customers = dao.find_all()
    return list(all_customers)
