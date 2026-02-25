Select
    student_id,
    min(exam_id) as exam_id,
    score
From
    exam_results
Where
    (student_id,score) in
            (Select student_id, max(score)
            from exam_results
            group by student_id)
Group by
    student_id,score
Order by
    student_id Asc;
