-- script that lists all genres from hbtn_0d_tvshows
--  and displays the number of shows linked to each.
SELECT g.name FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_g ON tv_s.id = tv_g.show_id
LEFT JOIN tv_genres AS g ON tv_g.genre_id = g.id
WHERE tv_s.title='Dexter';
