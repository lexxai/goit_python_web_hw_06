import logging
from sqlite3 import Cursor, Error

try:
    from connection import create_connection
except ImportError:
    from hw_06.connection import create_connection


logger = logging.getLogger(__name__)


def get_task_01(cur: Cursor) -> list[int]:
    sql = """
    SELECT s.fullname, AVG(grade) as AVG
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    GROUP BY s.id
    ORDER BY AVG DESC
    LIMIT 5
    """
    try:
        cur.execute(sql)
        res =  [v[:] for v in cur.fetchall()]
        return f"Studnts: {res}"
    except Error as e:
        logger.error(e)


def get_statitics():
    logger.debug("get_tasks")
    try:
        with create_connection() as conn:
            if conn is not None:
                cur: Cursor = conn.cursor()
                logger.info(get_task_01(cur))
                cur.close()
    except RuntimeError as err:
        logger.error(err)
