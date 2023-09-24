    SELECT d.name AS discipline, s.fullname as student, ROUND(AVG(grade),2) as average_garde
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    LEFT JOIN disciplines d ON g.disciplines_id = d.id 
    WHERE g.disciplines_id = 2
    GROUP BY s.id
    ORDER BY average_garde DESC
    LIMIT 1