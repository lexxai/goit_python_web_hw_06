SELECT d.name AS discipline, s.fullname as student, t.fullname AS teacher, ROUND(AVG(grade),2) as average_garde
FROM grade g
LEFT JOIN students s ON s.id = g.students_id 
LEFT JOIN disciplines d ON g.disciplines_id = d.id 
LEFT JOIN teachers t ON d.teachers_id = t.id 
WHERE s.id = 3 AND t.id = 1
GROUP BY discipline
ORDER BY average_garde DESC