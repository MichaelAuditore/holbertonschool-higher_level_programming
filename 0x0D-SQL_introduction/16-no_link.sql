-- GROUP BY SCORE AND CREATE A NEW COLUMN WHO COUNTS
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
