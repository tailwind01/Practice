SELECT 
    h.hacker_id, 
    h.name
FROM Hackers h
JOIN Submissions s ON h.hacker_id = s.hacker_id
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score -- Filter applied for full score
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.submission_id) > 1 -- Filter applied for more than 1 (greater than or equal to 2 submissions)
ORDER BY COUNT(s.submission_id) DESC, h.hacker_id ASC
