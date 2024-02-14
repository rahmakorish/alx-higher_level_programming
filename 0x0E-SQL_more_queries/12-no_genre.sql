-- script that lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
left JOIN tv_show_genres
ON tv_show_genres.genre_id = NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
