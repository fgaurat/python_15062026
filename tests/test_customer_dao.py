from pathlib import Path

import customer_dao
from customer import Customer
from customer_dao import CustomerDAO


def _build_dao_with_mocks(monkeypatch, mocker, rows):
    fake_cursor = mocker.Mock()
    fake_cursor.fetchall.return_value = rows

    fake_conn = mocker.Mock()
    fake_conn.cursor.return_value = fake_cursor

    connect_spy = mocker.Mock(return_value=fake_conn)
    monkeypatch.setattr(customer_dao.sqlite3, "connect", connect_spy)

    class FakeCustomer:
        def __init__(self, *values):
            self.values = values

    monkeypatch.setattr(customer_dao, "Customer", FakeCustomer)

    dao = CustomerDAO(Path("fake_db.sqlite"))
    return dao, fake_conn, fake_cursor, FakeCustomer, connect_spy


def test_old_find_all_returns_customers_list_in_order(monkeypatch, mocker):
    rows = [
        (1, "Alice", "Doe"),
        (2, "Bob", "Smith"),
    ]
    dao, _, _, fake_customer_cls, _ = _build_dao_with_mocks(
        monkeypatch, mocker, rows
    )

    result = dao.old_find_all()

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, fake_customer_cls) for item in result)
    assert [item.values for item in result] == rows


def test_old_find_all_executes_query_fetches_and_closes_cursor(monkeypatch, mocker):
    dao, _, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [(1, "X")])

    _ = dao.old_find_all()

    fake_cursor.execute.assert_called_once_with("SELECT * FROM customers_tbl")
    fake_cursor.fetchall.assert_called_once_with()
    fake_cursor.close.assert_called_once_with()


def test_old_find_all_returns_empty_list_when_no_data(monkeypatch, mocker):
    dao, _, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [])

    result = dao.old_find_all()

    assert result == []
    fake_cursor.close.assert_called_once_with()


def test_init_calls_sqlite_connect_with_given_path(monkeypatch, mocker):
    fake_conn = mocker.Mock()
    connect_spy = mocker.Mock(return_value=fake_conn)
    monkeypatch.setattr(customer_dao.sqlite3, "connect", connect_spy)

    db_path = Path("db/customers_db.db")
    _ = CustomerDAO(db_path)

    connect_spy.assert_called_once_with(db_path)


def test_find_by_id_returns_customer_when_row_exists(monkeypatch, mocker):
    rows = [(7, "Alice", "Doe", "alice@example.com", "F", "10.0.0.7")]
    dao, _, fake_cursor, fake_customer_cls, _ = _build_dao_with_mocks(
        monkeypatch, mocker, rows
    )
    fake_cursor.fetchone.return_value = rows[0]

    result = dao.find_by_id(7)

    fake_cursor.execute.assert_called_once_with(
        "SELECT * FROM customers_tbl WHERE id = ?", (7,)
    )
    fake_cursor.close.assert_called_once_with()
    assert isinstance(result, fake_customer_cls)
    assert result.values == rows[0]


def test_find_by_id_returns_none_when_row_missing(monkeypatch, mocker):
    dao, _, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [])
    fake_cursor.fetchone.return_value = None

    result = dao.find_by_id(999)

    assert result is None
    fake_cursor.close.assert_called_once_with()


def test_save_inserts_customer_when_id_is_not_set(monkeypatch, mocker):
    dao, fake_conn, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [])
    fake_cursor.lastrowid = 12

    customer = Customer(
        first_name="Ada",
        last_name="Lovelace",
        email="ada@example.com",
        gender="F",
        ip_address="10.0.0.12",
    )

    saved = dao.save(customer)

    fake_cursor.execute.assert_called_once_with(
        (
            "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) "
            "VALUES(?,?,?,?,?)"
        ),
        ("Ada", "Lovelace", "ada@example.com", "F", "10.0.0.12"),
    )
    fake_conn.commit.assert_called_once_with()
    fake_cursor.close.assert_called_once_with()
    assert saved == Customer(
        id=12,
        first_name="Ada",
        last_name="Lovelace",
        email="ada@example.com",
        gender="F",
        ip_address="10.0.0.12",
    )


def test_save_updates_customer_when_id_exists(monkeypatch, mocker):
    dao, fake_conn, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [])
    customer = Customer(
        id=3,
        first_name="Grace",
        last_name="Hopper",
        email="grace@example.com",
        gender="F",
        ip_address="10.0.0.3",
    )

    saved = dao.save(customer)

    fake_cursor.execute.assert_called_once_with(
        (
            "UPDATE customers_tbl SET first_name = ?, last_name = ?, email = ?, "
            "gender = ?, ip_address = ? WHERE id = ?"
        ),
        ("Grace", "Hopper", "grace@example.com", "F", "10.0.0.3", 3),
    )
    fake_conn.commit.assert_called_once_with()
    fake_cursor.close.assert_called_once_with()
    assert saved is customer


def test_delete_returns_true_when_row_deleted(monkeypatch, mocker):
    dao, fake_conn, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [])
    fake_cursor.rowcount = 1

    result = dao.delete(8)

    fake_cursor.execute.assert_called_once_with(
        "DELETE FROM customers_tbl WHERE id = ?", (8,)
    )
    fake_conn.commit.assert_called_once_with()
    fake_cursor.close.assert_called_once_with()
    assert result is True


def test_delete_returns_false_when_row_missing(monkeypatch, mocker):
    dao, fake_conn, fake_cursor, _, _ = _build_dao_with_mocks(monkeypatch, mocker, [])
    fake_cursor.rowcount = 0

    result = dao.delete(404)

    fake_cursor.execute.assert_called_once_with(
        "DELETE FROM customers_tbl WHERE id = ?", (404,)
    )
    fake_conn.commit.assert_called_once_with()
    fake_cursor.close.assert_called_once_with()
    assert result is False
