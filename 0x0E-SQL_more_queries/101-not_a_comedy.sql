-- List all genres not linked to the Dexter show
SELECT DISTINCT tv_shows.title FROM tv_shows JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id WHERE tv_genres.id NOT IN (SELECT id FROM tv_genres WHERE name = 'Comedy') ORDER BY tv_shows.title;
