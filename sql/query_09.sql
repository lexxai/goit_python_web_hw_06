SELECT  s.fullname as student, d.name AS discipline
FROM grade g
LEFT JOIN students s ON s.id = g.students_id 
LEFT JOIN disciplines d ON g.disciplines_id = d.id 
WHERE s.id = 3
GROUP BY discipline
ORDER BY discipline