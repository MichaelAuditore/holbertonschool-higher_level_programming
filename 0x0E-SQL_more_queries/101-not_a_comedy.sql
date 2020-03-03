-- script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT shows.title FROM tv_shows AS shows
LEFT JOIN (
	SELECT shows.id FROM tv_shows AS shows
	JOIN tv_show_genres AS show_genres ON show_genres.show_id = shows.id
	JOIN tv_genres AS genres ON genres.id = show_genres.genre_id AND genres.name = 'Comedy'
	ORDER BY shows.title ASC
) AS subquery
ON shows.id = subquery.id
WHERE subquery.id IS NULL
ORDER BY shows.title ASC;
