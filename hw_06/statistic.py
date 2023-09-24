import logging
from pathlib import Path
from sqlite3 import Cursor, Error

try:
    from connection import create_connection
except ImportError:
    from hw_06.connection import create_connection


logger = logging.getLogger(__name__)



def get_task(cur: Cursor, sql) -> list[int]:
    try:
        cur.execute(sql)
        res = cur.fetchall()
        # res =  [v[:] for v in cur.fetchall()]
        return res
    except Error as e:
        logger.error(e)






TASKS = ["01", "02"]


def get_statitics():
    logger.debug("get_tasks")
    query_base_path = Path("sql")   
    result = []
    try:
        with create_connection() as conn:
            if conn is not None:
                cur: Cursor = conn.cursor()
                for task in TASKS:
                    query_path = query_base_path.joinpath(f"query_{task}.sql")
                    if query_path.is_file():
                        logger.debug(f"START TASK {task}")
                        result.append((f"TASK {task}:", get_task(cur, query_path.read_text())))
                cur.close()
    except RuntimeError as err:
        logger.error(err)
    return result
