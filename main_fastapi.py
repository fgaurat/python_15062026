
from fastapi import FastAPI
from pathlib import Path
from customer_dao import CustomerDAO


app = FastAPI()

# fastapi dev main_fastapi.py
@app.get('/')
def hello():
    return {'Hello':"World"}

@app.get('/customers')
def get_customers():
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)
    all_customers = dao.find_all()
    return list(all_customers)


