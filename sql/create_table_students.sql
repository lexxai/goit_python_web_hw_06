DROP TABLE IF EXISTS students; 
CREATE TABLE students (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     fullname VARCHAR(120),
     group_id REFERENCES [groups](id)
);