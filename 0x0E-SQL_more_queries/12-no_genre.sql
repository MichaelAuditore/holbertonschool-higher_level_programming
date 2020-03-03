-- DISPLAYS SHOWS BY GENRE IN ASC
SELECT sh.title, g.genre_id FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS g 
ON g.show_id = sh.id WHERE g.genre_id IS NULL
ORDER BY sh.title, g.genre_id;
