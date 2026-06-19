import sqlite3
from collections.abc import Iterator
from pathlib import Path

from customer import Customer


class CustomerDAO:
    _SELECT_ALL_SQL = "SELECT * FROM customers_tbl"
    _SELECT_BY_ID_SQL = "SELECT * FROM customers_tbl WHERE id = ?"
    _INSERT_SQL = (
        "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) "
        "VALUES(?,?,?,?,?)"
    )
    _UPDATE_SQL = (
        "UPDATE customers_tbl "
        "SET first_name = ?, last_name = ?, email = ?, gender = ?, ip_address = ? "
        "WHERE id = ?"
    )
    _DELETE_SQL = "DELETE FROM customers_tbl WHERE id = ?"

    def __init__(self,db_path:Path) -> None:
        self._conn = sqlite3.connect(db_path)

    @staticmethod
    def _row_to_customer(row: tuple[int, str, str, str, str, str]) -> Customer:
        return Customer(*row)

    def old_find_all(self)->list[Customer]:
        cur = self._conn.cursor()

        cur.execute(self._SELECT_ALL_SQL)
        data = cur.fetchall()
        list_customers = [self._row_to_customer(row) for row in data]

        cur.close()
        return list_customers

    def find_all(self)->Iterator[Customer]:
        cur = self._conn.cursor()

        cur.execute(self._SELECT_ALL_SQL)
        data = cur.fetchall()

        for row in data:
            yield self._row_to_customer(row)
        cur.close()

    def find_by_id(self, customer_id: int) -> Customer | None:
        cur = self._conn.cursor()

        cur.execute(self._SELECT_BY_ID_SQL, (customer_id,))
        row = cur.fetchone()
        cur.close()

        if row is None:
            return None

        return self._row_to_customer(row)

    def save(self, customer: Customer) -> Customer:
        if customer.id <= 0:
            cur = self._conn.cursor()
            cur.execute(
                self._INSERT_SQL,
                (
                    customer.first_name,
                    customer.last_name,
                    customer.email,
                    customer.gender,
                    customer.ip_address,
                ),
            )
            self._conn.commit()
            row_id = cur.lastrowid
            assert row_id is not None
            customer.id = row_id
            cur.close()
        else:
            cur = self._conn.cursor()
            cur.execute(
                self._UPDATE_SQL,
                (
                    customer.first_name,
                    customer.last_name,
                    customer.email,
                    customer.gender,
                    customer.ip_address,
                    customer.id,
                ),
            )
            self._conn.commit()
            cur.close()
        return customer

    def delete(self, customer_id: int) -> bool:
        cur = self._conn.cursor()
        cur.execute(self._DELETE_SQL, (customer_id,))
        self._conn.commit()
        deleted = cur.rowcount > 0
        cur.close()
        return deleted

    def close(self) -> None:
        self._conn.close()

    def __del__(self) -> None:
        conn = getattr(self, "_conn", None)
        if conn is not None:
            conn.close()

def main() -> None:
    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)

    customer_list = dao.old_find_all()
    print(customer_list[12])

    customers_iter = dao.find_all()
    print(customers_iter)
    # d1 = next(customers)
    # print(d1)
    # d2 = next(customers)
    # print(d2)


    for customer in customers_iter:
        print(customer.first_name)
        print(customer)

if __name__=='__main__':
    main()
