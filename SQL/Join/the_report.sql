SELECT
    CASE WHEN Grade >= 8
        THEN Name
        ELSE NULL
    END,
    Grade, Marks
FROM Students
LEFT JOIN Grades
    ON Grades.Min_Mark <= Students.Marks AND Students.Marks <= Grades.Max_Mark
ORDER BY Grade DESC, Name, Marks;
