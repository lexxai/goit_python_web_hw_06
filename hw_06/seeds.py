import logging
from faker import Faker
from datetime import datetime, date, timedelta
from random import randint, sample
from sqlite3 import Cursor, Error

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
TOTAL_STUDENTS = 150
TOTAL_GRADES = 400

fake: Faker = Faker("uk-UA")


def seed_disciplines(cur: Cursor):
    sql = "INSERT INTO disciplines(name, teachers_id) VALUES (?,?);"
    try:
        cur.executemany(
            sql,
            zip(
                disciplines,
                iter([randint(1, TOTAL_TEACHERS) for _ in range(len(disciplines))]),
            ),
        )
    except Error as e:
        logger.error(e)


def seed_groups(cur: Cursor):
    sql = "INSERT INTO groups(name) VALUES (?);"
    try:
        cur.executemany(
            sql,
            zip(
                groups,
            ),
        )
    except Error as e:
        logger.error(e)


def seed_teacher(cur: Cursor):
    teachers = [
        fake.name().replace("пані", "").replace("пан", "").strip()
        for _ in range(TOTAL_TEACHERS)
    ]
    sql = "INSERT INTO teachers(fullname) VALUES (?);"
    try:
        cur.executemany(
            sql,
            zip(
                teachers,
            ),
        )
    except Error as e:
        logger.error(e)


def seed_students(cur: Cursor):
    students = [
        fake.name().replace("пані", "").replace("пан", "").strip()
        for _ in range(TOTAL_STUDENTS)
    ]
    sql = "INSERT INTO students(fullname, group_id) VALUES (?,?);"

    try:
        cur.executemany(
            sql,
            zip(
                students, iter([randint(1, len(groups)) for _ in range(TOTAL_STUDENTS)])
            ),
        )
    except Error as e:
        logger.error(e)


def get_group_students(cur: Cursor, group_id) -> list[int]:
    sql = "SELECT id FROM students WHERE group_id = ?;"
    try:
        cur.execute(sql, (group_id,))
        return [v[0] for v in cur.fetchall()]
    except Error as e:
        logger.error(e)


def seed_grade(cur: Cursor):
    satrt_date = datetime.strptime("2023-04-21", "%Y-%m-%d")
    end_date = datetime.strptime("2024-02-20", "%Y-%m-%d")

    def get_day() -> date:
        fake_day: date
        while True:
            fake_day = fake.date_between(satrt_date, end_date)
            if fake_day.isoweekday() < 6:
                break
        return fake_day

    grades = []
    sql = "INSERT INTO grade(grade, disciplines_id, students_id, date_of) VALUES (?, ?, ?, ?);"
    for _ in range(TOTAL_GRADES):
        random_discipline = randint(1, len(disciplines))
        random_group = randint(1, len(groups))
        # random_students = [randint(1, TOTAL_STUDENTS) for _ in range(randint(3, 12))]
        group_students = get_group_students(cur, random_group)
        max_random_students_in_group = min(12, len(group_students))
        min_random_students_in_group = min(3, len(group_students))
        random_students = sample(
            group_students,
            randint(min_random_students_in_group, max_random_students_in_group),
        )
        # random_students = []
        random_date_of = get_day()
        for random_student in random_students:
            random_grade = randint(30, 100)
            grades.append(
                (random_grade, random_discipline, random_student, random_date_of)
            )
    try:
        cur.executemany(sql, grades)
    except Error as e:
        logger.error(e)


def seeds():
    logger.debug("seeds data")
    try:
        with create_connection() as conn:
            if conn is not None:
                cur: Cursor = conn.cursor()
                seed_teacher(cur)
                seed_disciplines(cur)
                seed_groups(cur)
                seed_students(cur)
                seed_grade(cur)
                cur.close()

    except RuntimeError as err:
        logger.error(err)
