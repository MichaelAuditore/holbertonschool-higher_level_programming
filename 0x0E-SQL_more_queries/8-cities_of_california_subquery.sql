-- Select from multiple tables
SELECT c.id, c.name FROM cities AS c, states AS s
WHERE s.name = 'California';
