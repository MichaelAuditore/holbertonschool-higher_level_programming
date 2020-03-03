-- script that lists all genres from hbtn_0d_tvshows
--  and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(tv_g.show_id) AS number_of_shows FROM tv_shows AS tv_s
RIGHT JOIN tv_show_genres AS tv_g ON tv_s.id = tv_g.show_id
RIGHT JOIN tv_genres AS g ON tv_g.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
