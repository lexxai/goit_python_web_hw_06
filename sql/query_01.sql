    SELECT s.fullname as student, ROUND(AVG(grade),2) as average_grade
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5