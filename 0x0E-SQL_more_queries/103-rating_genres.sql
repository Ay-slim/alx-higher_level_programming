-- Aggregate tv show genre ratings
SELECT tv_genres.name, SUM(rate) AS rating FROM tv_shows JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.show_id JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id  GROUP BY tv_genres.name ORDER BY rating DESC;
