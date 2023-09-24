    SELECT s.fullname, ROUND(AVG(grade),2) as AVG
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    GROUP BY s.id
    ORDER BY AVG DESC
    LIMIT 5