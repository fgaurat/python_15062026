
# Formation Python 15/06/2026

Ce dépôt regroupe les exercices, démonstrations et mini-projets utilisés pendant une formation Python.
Il couvre plusieurs thèmes du langage et de l'écosystème : bases du langage, structures de données, programmation orientée objet, accès SQLite, scripts réseau, interfaces graphiques, web apps, traitement asynchrone et tâches en arrière-plan.

## Objectif du projet

Le but de ce dépôt n'est pas de fournir une application unique, mais un terrain d'entraînement avec des exemples indépendants.
Chaque fichier illustre une notion précise ou une petite combinaison de notions.

## Pré-requis

- Python 3.10 ou plus récent
- Un environnement virtuel local
- Les dépendances déclarées dans [pyproject.toml](pyproject.toml)

## Installation

Créer et activer un environnement virtuel, puis installer le projet en mode développement :

```bash
python -m venv .venv
source .venv/bin/activate
.venv/bin/python -m pip install -e ".[dev]"
```

Si tu utilises déjà l'environnement virtuel fourni dans le dépôt, tu peux passer directement aux commandes ci-dessous.

## Commandes utiles

Tests :

```bash
.venv/bin/python -m pytest
```

Lint :

```bash
.venv/bin/python -m ruff check .
```

Typage :

```bash
.venv/bin/python -m mypy .
```

## Organisation du dépôt

### Fondamentaux du langage

- [control_flow.py](control_flow.py)
- [data_structure_dict.py](data_structure_dict.py)
- [data_structure_list.py](data_structure_list.py)
- [data_structure_set.py](data_structure_set.py)
- [data_structure_tuple.py](data_structure_tuple.py)
- [hello.py](hello.py)
- [fibo.py](fibo.py)
- [fibo_propre.py](fibo_propre.py)
- [main_input_output.py](main_input_output.py)
- [main_error.py](main_error.py)

### POO et géométrie

- [icalcgeo.py](icalcgeo.py)
- [rectangle.py](rectangle.py)
- [carre.py](carre.py)
- [cercle.py](cercle.py)
- [oldrectangle.py](oldrectangle.py)
- [rectangle_main.py](rectangle_main.py)
- [rectangle_sale.py](rectangle_sale.py)

### Données et SQLite

- [customer.py](customer.py)
- [customer_dao.py](customer_dao.py)
- [main_import.py](main_import.py)
- [MOCK_DATA.csv](MOCK_DATA.csv)
- [db/](db/)

### Web et API

- [app_flask.py](app_flask.py)
- [main_fastapi.py](main_fastapi.py)
- [main_streamlit.py](main_streamlit.py)
- [templates/](templates/)
- [pages/](pages/)

### Réseau, asynchrone et traitements parallèles

- [main_requests.py](main_requests.py)
- [main_requests_async.py](main_requests_async.py)
- [main_requests_async_queues.py](main_requests_async_queues.py)
- [main_async.py](main_async.py)
- [main_multiprocess.py](main_multiprocess.py)
- [main_multithread.py](main_multithread.py)
- [main_cpu_bound.py](main_cpu_bound.py)
- [celery_main.py](celery_main.py)
- [celery_tasks.py](celery_tasks.py)

### Interfaces graphiques

- [main_qt.py](main_qt.py)
- [main_tk.py](main_tk.py)
- [main.ui](main.ui)
- [chat.gif](chat.gif)

### Données de démonstration

- [users.json](users.json)
- [todos.json](todos.json)
- [data.json](data.json)
- [le_fichier.txt](le_fichier.txt)
- [customers.rest](customers.rest)

### Tests

- [tests/](tests/)

## Exemples d'exécution

### Script Fibonacci

```bash
.venv/bin/python fibo_propre.py
```

### Flask

```bash
.venv/bin/python -m flask --app app_flask run --debug
```

### FastAPI

```bash
.venv/bin/python -m uvicorn main_fastapi:app --reload
```

### Streamlit

```bash
.venv/bin/python -m streamlit run main_streamlit.py
```

### Gestion des données SQLite

Le fichier [main_import.py](main_import.py) charge [MOCK_DATA.csv](MOCK_DATA.csv) dans la base SQLite locale `db/customers_db.db`.

Les exemples Flask, FastAPI et Streamlit s'appuient sur cette base.

## Tests

La suite de tests est basée sur `pytest`.

```bash
.venv/bin/python -m pytest
```

Les tests couvrent notamment :

- les exemples de géométrie et de POO
- le DAO SQLite client
- les comportements exposés par certaines apps de démonstration

## Qualité de code

Le dépôt utilise `ruff` pour le lint et `mypy` pour le typage.

Commandes recommandées :

```bash
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy .
```

Note : `mypy .` peut signaler un conflit de module entre [main_fibo.py](main_fibo.py) et [demo_module/main_fibo.py](demo_module/main_fibo.py). C'est un point connu du dépôt de formation.

## Structure générale

Le dépôt suit une organisation plate : les modules principaux sont à la racine, avec quelques dossiers dédiés aux tests, aux templates, aux pages Streamlit et aux données SQLite.

## Remarques pédagogiques

- Certains fichiers sont volontairement simples ou redondants pour illustrer différentes approches.
- Plusieurs scripts sont des démonstrations indépendantes et ne sont pas conçus comme une application unique.
- Le style de code peut évoluer au fil des exercices.



## Ressources utiles

https://github.com/fgaurat/python_15062026


https://docadmin.orsys.fr/.
Le mot de passe de connexion que vous devez communiquer aux participants : aFx9auyQU


https://docs.python.org/3/tutorial/index.html



https://peps.python.org/pep-0008/
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/index.html


https://refactoring.guru/fr

https://wiki.python.org/moin/TimeComplexity.html

https://docs.python.org/3/tutorial/datastructures.html#sets

https://www.mockaroo.com/


https://docs.python.org/3/library/csv.html#csv.DictReader


https://jsonplaceholder.typicode.com/


https://jsonplaceholder.typicode.com/todos

https://jsonplaceholder.typicode.com/users

https://realpython.com/

https://www.stashofcode.fr/comment-marche-fonction-super-de-python/

https://sqlitebrowser.org/

https://docs.python.org/3/library/pathlib.html#basic-use


https://docs.python.org/3/library/sqlite3.html



https://www.toptal.com/developers/gitignore/

https://flask.palletsprojects.com/en/stable/installation/
https://flask.palletsprojects.com/en/stable/quickstart/


https://jinja.palletsprojects.com/en/stable/templates/
https://getbootstrap.com/


https://fastapi.tiangolo.com/#example

https://docs.streamlit.io/


https://docs.streamlit.io/develop/api-reference/widgets/st.text_input


https://logs.eolem.com/

https://requests.readthedocs.io/en/latest/user/install/#install


https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup



https://docs.python.org/3/library/asyncio.html


https://www.python-httpx.org/async/


https://excalidraw.com/#json=2APgNcevAYZRWOYMKZEEJ,BXCeeBK_bDpLk491kYG0xA
