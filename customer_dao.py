import sqlite3
from pathlib import Path
from customer import Customer
from typing import List,Iterator

class CustomerDAO:

    def __init__(self,db_path:Path) -> None:
        self._conn = sqlite3.connect(db_path)

    def old_find_all(self)->List[Customer]:
        sql = "SELECT * FROM customers_tbl"
        cur = self._conn.cursor()
        
        cur.execute(sql)
        data = cur.fetchall()
        list_customers=[]
        for d in data:
            c = Customer(*d)
            list_customers.append(c)
        
        cur.close()
        return list_customers
    

    

    def find_all(self)->Iterator[Customer]:
        sql = "SELECT * FROM customers_tbl"
        cur = self._conn.cursor()
        
        cur.execute(sql)
        data = cur.fetchall()
    
        for d in data:
            c = Customer(*d)
            yield c
        cur.close()

    
    def __del__(self):
        self._conn.close()

def main():
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)

    customers = dao.old_find_all()
    print(customers[12])
    
    customers = dao.find_all()
    print(customers)
    # d1 = next(customers)
    # print(d1)
    # d2 = next(customers)
    # print(d2)


    for customer in customers:
        print(customer.first_name)
        print(customer)

if __name__=='__main__':
    main()
