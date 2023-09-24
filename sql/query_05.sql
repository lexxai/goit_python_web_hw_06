SELECT t.fullname AS teacher, d.name AS discipline
FROM grade g 
LEFT JOIN disciplines d ON g.disciplines_id  = d.id 
LEFT JOIN teachers t ON d.teachers_id = t.id 
WHERE t.id = 1
GROUP BY d.id
