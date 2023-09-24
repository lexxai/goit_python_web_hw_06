import logging
from pathlib import Path
from pprint import pprint
from faker import Faker
import rich

try:
    from create_tables import create_tables
    from seeds import seeds
    from statistic import get_statitics
except ImportError:
    from hw_06.create_tables import create_tables
    from hw_06.seeds import seeds
    from hw_06.statistic import get_statitics


def print_results(results: list):
    if results:
        rich.print("[yellow]Result of statistics tasks:[/yellow]")
        for result in results:
            rich.print(result)
    else:
        rich.print("[red]Result of statistics empty[/red]")


def main():
    skip_created_tables = True
    if create_tables(skip_created_tables):
        if not skip_created_tables:
            seeds()
        results = get_statitics()
        print_results(results)

    

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    FORMAT = "%(asctime)s  %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    main()


