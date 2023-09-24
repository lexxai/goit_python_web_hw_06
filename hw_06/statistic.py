import logging
from sqlite3 import Cursor, Error

try:
    from connection import create_connection
except ImportError:
    from hw_06.connection import create_connection


logger = logging.getLogger(__name__)



def get_task_01(cur: Cursor) -> list[int]:
    sql = """
    SELECT s.fullname, ROUND(AVG(grade),2) as AVG
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    GROUP BY s.id
    ORDER BY AVG DESC
    LIMIT 5
    """
    try:
        cur.execute(sql)
        res = cur.fetchall()
        # res =  [v[:] for v in cur.fetchall()]
        return res
    except Error as e:
        logger.error(e)



TASKS = {
    "TASK_01": get_task_01
}


def get_statitics():
    logger.debug("get_tasks")
    result = []
    try:
        with create_connection() as conn:
            if conn is not None:
                cur: Cursor = conn.cursor()
                for task, task_fuc in TASKS.items():
                    result.append((task, task_fuc(cur)))
                cur.close()
    except RuntimeError as err:
        logger.error(err)
    return result
