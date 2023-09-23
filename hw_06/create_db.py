import logging
from sqlite3 import Error


logger = logging.getLogger(__name__)


def create_table(conn, sql_expression):
    c = conn.cursor()
    try:
        c.executescript(sql_expression)
        conn.commit()
    except Error as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()






