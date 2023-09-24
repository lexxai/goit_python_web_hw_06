import logging
from pathlib import Path
from faker import Faker

try:
    from create_tables import create_tables
    from seeds import seeds
    from statistic import get_statitics
except ImportError:
    from hw_06.create_tables import create_tables
    from hw_06.seeds import seeds
    from hw_06.statistic import get_statitics



def main():
    if create_tables():
        seeds()
        get_statitics()

    

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    FORMAT = "%(asctime)s  %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    main()


