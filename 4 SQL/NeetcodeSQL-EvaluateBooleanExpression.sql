-- Neetcode uses PostgreSQL

SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE 
        WHEN e.operator = '>' THEN v1.value > v2.value
        WHEN e.operator = '<' THEN v1.value < v2.value
        WHEN e.operator = '=' THEN v1.value = v2.value
        ELSE FALSE
    END AS value
FROM Expressions e
JOIN Variables v1 ON e.left_operand = v1.name
JOIN Variables v2 ON e.right_operand = v2.name;
