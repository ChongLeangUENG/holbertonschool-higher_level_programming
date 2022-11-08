-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS number_of_shows -- Query to join tables
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.show_id
ORDER BY number_of_shows DESC, tv_genres.id ASC;