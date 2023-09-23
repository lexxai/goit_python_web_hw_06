DROP TABLE IF EXISTS grade; 
CREATE TABLE grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grade INTEGER, 
    disciplines_id REFERENCES disciplines (id),
    students_id REFERENCES students (id),
    date_of DATE
);