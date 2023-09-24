SELECT gr.name as [group] , s.fullname as student, REVERSE(SUBSTR(REVERSE(s.fullname), 0, CHARINDEX(' ', REVERSE(s.fullname)))) AS last_name
FROM students s
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE group_id = 1
ORDER BY last_name


-- SELECT gr.name as [group] , s.fullname as student, REVERSE(s.fullname) AS LN
-- FROM students s
-- LEFT JOIN groups gr ON s.group_id = gr.id 
-- WHERE group_id = 1
-- ORDER BY student
-- -- REVERSE(SUBSTRING(REVERSE(s.fullname), 0, CHARINDEX('' , REVERSE(s.fullname))))

