-- Задание 2.1
SELECT song_name, song_duration
FROM songs
ORDER BY song_duration DESC
LIMIT 1

-- Задание 2.2
SELECT song_name
FROM songs
WHERE song_duration >= 210

-- Задание 2.3
SELECT collection_name
FROM collection
WHERE date_release BETWEEN '2018-01-01' AND '2020-12-31'

-- Задание 2.4
SELECT singer_name
FROM singers
WHERE singer_name NOT LIKE '% %'

-- Задание 2.5
SELECT song_name FROM songs
WHERE string_to_array(LOWER(song_name), ' ') && ARRAY['мой', 'my']

-- Задание 3.1
SELECT genre.genre_name, COUNT(singer_id) FROM genre
LEFT JOIN singers_genre ON genre.genre_id = singers_genre.genre_id
GROUP BY genre.genre_name

-- Задание 3.2
SELECT COUNT(song_name) FROM songs
LEFT JOIN albums ON songs.album_id = albums.album_id
WHERE albums.year_of_release BETWEEN '2019-01-01' AND '2020-12-31'

-- Задание 3.3
SELECT albums.album_name, AVG(song_duration) FROM songs
LEFT JOIN albums ON albums.album_id = songs.album_id
GROUP BY albums.album_name
ORDER BY AVG(song_duration)

-- Задание 3.4
SELECT singer_name 
FROM singers
WHERE singer_id NOT IN (
	SELECT singer_id FROM singers_album
	JOIN albums ON singers_album.album_id = albums.album_id
	WHERE albums.year_of_release >= '2020-01-01' AND albums.year_of_release < '2021-01-01'
	);

-- Задание 3.5
SELECT collection_name FROM collection
JOIN songs_collection ON collection.collection_id = songs_collection.collection_id
JOIN songs ON songs_collection.song_id = songs.song_id
JOIN albums ON songs.album_id = albums.album_id
JOIN singers_album ON albums.album_id = singers_album.album_id
JOIN singers ON singers_album.singer_id = singers.singer_id
WHERE singer_name LIKE 'Michael Jackson'
GROUP BY collection_name

