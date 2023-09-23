import logging
from pathlib import Path

try:
    from connection import create_connection
    from create_db import executescript
except ImportError:
    from hw_06.connection import create_connection
    from hw_06.create_db import executescript


logger = logging.getLogger(__name__)

def create_tables() -> bool:
    result = False
    logger.debug("create_tables")
    tables_path = Path("sql")
    tables = [
        "create_table_groups.sql",
        "create_table_students.sql",
        "create_table_disciplies.sql",
        "create_table_teachers.sql",
        "create_table_grade.sql"
    ]
    try:
        with create_connection() as conn:
            if conn is not None:
                for table in tables:
                    try:
                        sql_script = tables_path.joinpath(table).read_text(encoding='utf-8')
                        # logger.info(f"{sql_script=}")
                    except OSError as e:
                        logger.error(f"ERROR OPEN SQL : {e}")
                        raise RuntimeError
                    else:
                        if sql_script:
                            if not executescript(conn, sql_script):
                                logger.error(f'Error: can\'t execute sql script: {table}')
                                raise RuntimeError
                logger.debug(f"All {len(tables)} tables created")
                result = True
            else:
                logger.error('Error: can\'t create the database connection')
    except RuntimeError as err:
        logger.error(err)
    return result