"""Corrigé — tests CustomerDAO (fixture in-memory + mock) (TP 6.3)."""

from unittest.mock import MagicMock

from customer import Customer
from customer_dao import CustomerDAO


def make_dao_with_conn(conn) -> CustomerDAO:
    dao = CustomerDAO.__new__(CustomerDAO)
    dao._conn = conn
    return dao


def test_find_all_avec_memory_db(memory_db):
    dao = make_dao_with_conn(memory_db)
    clients = list(dao.find_all())
    assert len(clients) == 3
    assert clients[0] == Customer(1, "Ada", "Lovelace", "ada@x.io", "F", "10.0.0.1")


def test_find_all_avec_mock():
    fake_rows = [
        (1, "Ada", "Lovelace", "ada@x.io", "F", "10.0.0.1"),
        (2, "Alan", "Turing", "alan@x.io", "M", "10.0.0.2"),
    ]
    cursor = MagicMock()
    cursor.fetchall.return_value = fake_rows
    conn = MagicMock()
    conn.cursor.return_value = cursor

    dao = make_dao_with_conn(conn)
    clients = list(dao.find_all())

    assert len(clients) == 2
    assert clients[0] == Customer(1, "Ada", "Lovelace", "ada@x.io", "F", "10.0.0.1")
    conn.cursor.assert_called_once()
    cursor.execute.assert_called_once()


def test_find_by_id_avec_memory_db(memory_db):
    dao = make_dao_with_conn(memory_db)

    client = dao.find_by_id(2)

    assert client == Customer(2, "Alan", "Turing", "alan@x.io", "M", "10.0.0.2")


def test_find_by_id_renvoie_none_si_absent(memory_db):
    dao = make_dao_with_conn(memory_db)

    client = dao.find_by_id(999)

    assert client is None


def test_save_insere_un_nouveau_client(memory_db):
    dao = make_dao_with_conn(memory_db)
    nouveau = Customer(
        first_name="Katherine",
        last_name="Johnson",
        email="katherine@x.io",
        gender="F",
        ip_address="10.0.0.4",
    )

    saved = dao.save(nouveau)

    assert saved.id > 0
    assert saved.first_name == "Katherine"
    assert dao.find_by_id(saved.id) == saved


def test_save_met_a_jour_un_client_existant(memory_db):
    dao = make_dao_with_conn(memory_db)
    client = dao.find_by_id(1)
    assert client is not None
    client.email = "ada.lovelace@x.io"

    saved = dao.save(client)

    assert saved.email == "ada.lovelace@x.io"
    assert dao.find_by_id(1) == saved


def test_delete_supprime_un_client(memory_db):
    dao = make_dao_with_conn(memory_db)

    deleted = dao.delete(3)

    assert deleted is True
    assert dao.find_by_id(3) is None


def test_delete_renvoie_false_si_absent(memory_db):
    dao = make_dao_with_conn(memory_db)

    deleted = dao.delete(404)

    assert deleted is False
