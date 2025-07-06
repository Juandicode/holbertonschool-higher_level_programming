-- Making a script that shows all elements in a list and counts the elements from other table that matches with them
SELECT tv_genres.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;