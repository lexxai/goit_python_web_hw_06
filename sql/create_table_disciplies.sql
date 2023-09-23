DROP TABLE IF EXISTS disciplines; 
CREATE TABLE disciplines (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name STRING UNIQUE,
     teachers_id REFERENCES teachers (id)
);