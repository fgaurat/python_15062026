import sqlite3
from pathlib import Path
from customer import Customer


class CustomerDAO:


    def __init__(self,db_path:Path) -> None:
        self._conn = sqlite3.connect(db_path)

    def find_all(self)->list[Customer]:
        sql = "SELECT * FROM customers_tbl"
        cur = self._conn.cursor()
        
        cur.execute(sql)
        data = cur.fetchall()
        list_customers=[]
        for d in data:
            c = Customer(*d)
            list_customers.append(c)

        return list_customers
    
    def __del__(self):
        self._conn.close()

def main():
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)

    customers = dao.find_all()
    # for customer in customers:
    #     print(customer.first_name)
    #     print(customer)

if __name__=='__main__':
    main()
