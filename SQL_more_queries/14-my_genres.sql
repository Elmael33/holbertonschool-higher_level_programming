-- List genres of the show Dexter
SELECT g.name
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres g ON tsg.genre_id = g.id
WHERE ts.title = 'Dexter'
ORDER BY g.name ASC;