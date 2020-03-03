-- Show ratings for shows
SELECT genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_show_ratings, tv_shows
JOIN tv_show_genres AS show_genres ON tv_shows.id = show_genres.show_id
JOIN tv_genres AS genres ON genres.id = show_genres.genre_id
WHERE tv_show_ratings.show_id = tv_shows.id
GROUP BY genres.name
ORDER BY rating DESC;
