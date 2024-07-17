<<<<<<< HEAD
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT s.title, g.genre_id
    FROM tv_shows AS s
        INNER JOIN tv_show_genres AS g ON s.id = g.show_id
    ORDER BY s.title, g.genre_id;
=======
-- List all shows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
>>>>>>> d0d761e514b0321d43719afdee8776985f533d1f
