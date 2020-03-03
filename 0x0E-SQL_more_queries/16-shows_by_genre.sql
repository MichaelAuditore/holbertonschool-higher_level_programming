-- script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT shows.title, genres.name FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres ON show_genres.show_id = shows.id
LEFT JOIN tv_genres AS genres ON genres.id = show_genres.genre_id
ORDER BY shows.title, genres.name ASC;
