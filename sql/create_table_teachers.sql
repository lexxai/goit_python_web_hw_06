DROP TABLE IF EXISTS teachers; 
CREATE TABLE teachers (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     fullname STRING
     disciplines_id REFERENCES disciplines (id)
);