import logging
from pathlib import Path


from sqlite3 import connect, OperationalError
from contextlib import contextmanager


logger = logging.getLogger(__name__)

@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    try:
        # conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='567234')
        database_path = Path("db")
        database_path.mkdir(exist_ok=True, parents=True)
        conn = connect(database_path.joinpath("hw06.sqlite"))
        yield conn
        conn.close()
    except OperationalError as err:
        raise RuntimeError(f"Failed to connect to the database: {err}")

