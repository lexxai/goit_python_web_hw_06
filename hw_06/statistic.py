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
        # res = cur.fetchall()
        res = [ dict(line) for line in [zip([ column[0] for column in cur.description], row) for row in cur.fetchall()] ]
        # res =  [v[:] for v in cur.fetchall()]
        return res
    except Error as e:
        logger.error(e)





def get_statitics():
    logger.debug("Get statitics")
    query_base_path = Path("sql")   
    result = []
    try:
        with create_connection() as conn:
            if conn is not None:
                cur: Cursor = conn.cursor()
                TASKS = query_base_path.glob("query_*.sql")
                for task in TASKS:
                    # query_path = query_base_path.joinpath(f"query_{task}.sql")
                    query_path = task
                    if query_path.is_file():
                        logger.debug(f"START TASK {task}")
                        result.append((f"TASK {task.stem}:", get_task(cur, query_path.read_text())))
                logger.debug(f"ALL TASKS FINISHED")
                cur.close()
    except RuntimeError as err:
        logger.error(err)
    return result
