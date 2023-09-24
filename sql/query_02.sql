    SELECT s.fullname, ROUND(AVG(grade),2) as AVG, d.name AS discipline
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    LEFT JOIN disciplines d ON g.disciplines_id = d.id 
    WHERE g.disciplines_id = 1
    ORDER BY AVG DESC
    LIMIT 5