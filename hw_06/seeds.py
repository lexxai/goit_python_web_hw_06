import logging
from faker import Faker
from datetime import datetime
from random import randint, choice
import sqlite3

try:
    from connection import create_connection
except ImportError:
    from hw_06.connection import create_connection


logger = logging.getLogger(__name__)


disciplines = [
    "Python Core",
    "Python Web",
    "Python Data Science",
    "Вища математика",
    "HTML CSS",
    "Soft Skils",
    "Databases SQL, noSQL",
    "English",
    "Git",
    "Історія України",
    "Ділова українська мова",
    "Філософія",
]

groups = [
    "M88-1/8",
    "M88-2/8",
    "M89-1/8",
    "M89-2/8",
    "C88-1/8",
    "C88-2/8",
    "C89-1/8",
    "C89-2/8",
    "P88-1/8",
    "P88-2/8",
    "P89-1/8",
    "P89-2/8",
]

TOTAL_TEACHERS = 10
TOTAL_STUDENDS = 150

fake: Faker = Faker("uk-UA")


def seed_disciplines(cur: sqlite3.Cursor):
    sql = 'INSERT INTO disciplines(name, teachers_id) VALUES (?,?);'
    try:
        cur.executemany(sql, zip(disciplines, [ randint(1,TOTAL_TEACHERS)  for _ in range(TOTAL_TEACHERS)] ))
    except sqlite3.ProgrammingError as e:
        logger.error(e)


def seed_groups(cur: sqlite3.Cursor):
    sql = 'INSERT INTO groups(name) VALUES (?);'
    try:
        cur.executemany(sql, zip(groups,))
    except sqlite3.ProgrammingError as e:
        logger.error(e)


def seed_teacher(cur: sqlite3.Cursor):
    teachers = [fake.name().replace("пані","").replace("пан","") for _ in range(TOTAL_TEACHERS)]
    sql = 'INSERT INTO teachers(fullname) VALUES (?);'
    try:
        cur.executemany(sql, zip(teachers,))
    except sqlite3.ProgrammingError as e:
        logger.error(e)

def seed_students(cur: sqlite3.Cursor):
    students = [fake.name().replace("пані","").replace("пан","") for _ in range(TOTAL_STUDENDS)]
    sql = 'INSERT INTO disciplines(name, teachers_id) VALUES (?,?);'

    try:
        cur.executemany(sql, zip(students, [ randint(1,len(groups))  for _ in groups] ))
    except sqlite3.ProgrammingError as e:
        logger.error(e)

def seed_disciplines(cur: sqlite3.Cursor):
    sql = 'INSERT INTO disciplines(name, teachers_id) VALUES (?,?);'
    try:
        cur.executemany(sql, zip(disciplines, [ randint(1,TOTAL_TEACHERS)  for _ in range(TOTAL_TEACHERS)] ))
    except sqlite3.ProgrammingError as e:
        logger.error(e)



def seeds():
    logger.debug("insert_data")
    try:
        with create_connection() as conn:
            if conn is not None:
                cur: sqlite3.Cursor =  conn.cursor()
                seed_disciplines(cur)
                seed_groups(cur)
                seed_teacher(cur)
                seed_students(cur)
                cur.close()

    except RuntimeError as err:
        logger.error(err)
