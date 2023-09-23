import logging
from sqlite3 import Error, Connection


logger = logging.getLogger(__name__)


def executescript(conn: Connection, sql_expression: str) -> bool:
    c = conn.cursor()
    result = False
    try:
        c.executescript(sql_expression)
        conn.commit()
        result = True
    except Error as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()
    return result






