import logging
from pathlib import Path
from faker import Faker

try:
    from connection import create_connection
except ImportError:
    from hw_06.connection import create_connection


logger = logging.getLogger(__name__)


def insert_data():
    logger.debug("insert_data")
    try:
        with create_connection() as conn:
            if conn is not None:
                ...
    except RuntimeError as err:
        logger.error(err)