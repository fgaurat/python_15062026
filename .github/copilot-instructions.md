# Copilot Instructions

## Commands

```bash
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/python -m pytest
.venv/bin/python -m pytest tests/test_rectangle.py
.venv/bin/python -m pytest tests/test_rectangle.py::test_surface
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy .
```

Current baseline:

- `pytest` is configured in `pyproject.toml` and runs `tests/`, but the full suite currently errors on `tests/test_customer_dao_unittest.py::test_find_all_avec_memory_db` because the `memory_db` fixture is missing.
- `ruff check .` is the configured linter, but the repository currently has many pre-existing lint findings across example scripts.
- `mypy .` is configured in strict mode, but currently stops on the duplicate module name `main_fibo` / `demo_module/main_fibo.py`.

## High-level architecture

This repository is a training/workshop codebase, not a single packaged application. Most Python files at the repository root are standalone examples grouped by topic (`main_*.py`, `data_structure_*.py`, `control_flow.py`, GUI/async/perf demos, etc.).

There are two reusable mini-domains that show up across multiple files:

1. Geometry/OOP examples: `icalcgeo.py` defines the abstract surface contract, `rectangle.py` implements it, and `carre.py` extends `Rectangle`. The corresponding pytest coverage lives in `tests/test_rectangle.py` and `tests/test_carre.py`.
2. Customer data examples: `customer.py` defines the dataclass and `customer_dao.py` reads from `db/customers_db.db`. That DAO is reused by the Flask app (`app_flask.py` + `templates/customers.html`), the FastAPI app (`main_fastapi.py`), and the Streamlit app (`main_streamlit.py` + `pages/`).
3. Database bootstrap is separate from the apps: `main_import.py` loads `MOCK_DATA.csv` and inserts rows into `customers_tbl` inside `db/customers_db.db`. The web/API demos assume that SQLite file is already populated.

Other areas such as Celery (`celery_main.py`, `celery_tasks.py`) and the async/request scripts are independent demos rather than shared infrastructure.

## Key conventions

- The repo uses a flat module layout from the repository root, not `src/` packaging. Imports are direct (`from rectangle import Rectangle`), and pytest relies on `pythonpath = ["."]` from `pyproject.toml`.
- Prefer the repository-local virtualenv at `.venv/` when running commands; the checked environment in this repo already uses it.
- Run commands from the repository root. Several scripts open files with relative paths such as `Path("db") / "customers_db.db"`, `todos.json`, `users.json`, and assets like `chat.gif`.
- For the customer example flow, prefer reusing `Customer` and `CustomerDAO` instead of duplicating data-access logic. The DAO now covers the basic CRUD path used in exercises: `find_all()`, `find_by_id()`, `save()`, and `delete()`.
- `CustomerDAO` currently exposes two read paths on purpose: `old_find_all()` returns a materialized list, while `find_all()` is the version reused by the apps and tests. Keep both unless the exercise explicitly asks to remove the legacy path.
- `find_all()` still does `fetchall()` before yielding `Customer(*row)` objects, so it behaves like a generator facade over an eager SQLite read rather than true streaming. Preserve that behavior unless you update every caller and test that depends on it.
- `save()` is an upsert-style method for the exercises: it inserts when `customer.id <= 0`, mutates the passed `Customer` with the generated `id`, and otherwise updates the existing row.
- DAO tests are split between monkeypatched connection tests (`tests/test_customer_dao.py`) and connection-injection tests built with `CustomerDAO.__new__` (`tests/test_customer_dao_unittest.py`). Follow those patterns when changing constructor or query behavior.
- The DAO maps `SELECT * FROM customers_tbl` rows positionally into the `Customer` dataclass. Changes to SQL column order or dataclass field order will ripple into Flask/FastAPI/Streamlit outputs and the existing DAO tests.
- Preserve the local style of the file you touch: this codebase mixes English module names with French comments, test names, and user-facing strings.
- Validation in the geometry examples is done with `assert` statements, and the existing tests expect `AssertionError` rather than custom exceptions.



