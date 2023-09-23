import logging
from pathlib import Path

try:
    from connection import create_connection
    from create_db import create_table
except ImportError:
    from hw_06.connection import create_connection
    from hw_06.create_db import create_table




def create_tables():
    logger.info("create_tables")
    tables_path = Path("sql")
    tables = [
        "create_table_groups.sql",
        "create_table_students.sql",
    ]
    try:
        with create_connection() as conn:
            if conn is not None:
                for table in tables:
                    try:
                        sql_expression = tables_path.joinpath(table).read_text(encoding='utf-8')
                        logger.info(f"{sql_expression=}")
                    except OSError as e:
                        logger.error(f"ERROR OPEN SQL : {e}")
                    else:
                        if sql_expression:
                            create_table(conn, sql_expression)
            else:
                logger.error('Error: can\'t create the database connection')
    except RuntimeError as err:
        logger.error(err)



def main():
    create_tables()

    

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    FORMAT = "%(asctime)s  %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    main()


