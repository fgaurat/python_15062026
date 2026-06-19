import sqlite3

import pytest


@pytest.fixture
def memory_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE customers_tbl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            gender TEXT,
            ip_address TEXT
        )
        """
    )
    cur.executemany(
        """
        INSERT INTO customers_tbl(first_name, last_name, email, gender, ip_address)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            ("Ada", "Lovelace", "ada@x.io", "F", "10.0.0.1"),
            ("Alan", "Turing", "alan@x.io", "M", "10.0.0.2"),
            ("Grace", "Hopper", "grace@x.io", "F", "10.0.0.3"),
        ],
    )
    conn.commit()
    yield conn
    conn.close()
