CREATE TABLE IF NOT EXISTS Singers (
	Singer_id SERIAL PRIMARY KEY,
	Singer_name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre(
	Genre_id SERIAL PRIMARY KEY,
	Genre_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Singers_genre(
	Singer_id INTEGER REFERENCES Singers(Singer_id),
	Genre_id INT REFERENCES Genre(Genre_id),
	CONSTRAINT pk PRIMARY KEY (Singer_id, Genre_id)
);

CREATE TABLE IF NOT EXISTS Albums(
	Album_id SERIAL PRIMARY KEY,
	Album_name VARCHAR(40) NOT NULL,
	Year_of_release DATE
);

CREATE TABLE IF NOT EXISTS Singers_album(
	Singer_id INTEGER REFERENCES Singers(Singer_id),
	Album_id INTEGER REFERENCES Albums(Album_id),
	CONSTRAINT pk_singers_album PRIMARY KEY (Singer_id, Album_id)
);

CREATE TABLE IF NOT EXISTS Songs(
	Song_id SERIAL PRIMARY KEY,
	Song_name VARCHAR(60) NOT NULL,
	Song_duration INT,
	Album_id INT REFERENCES Albums(Album_id)
);

CREATE TABLE IF NOT EXISTS Collection(
	Collection_id SERIAL PRIMARY KEY,
	Collection_name VARCHAR(60) NOT NULL,
	Date_release DATE
);

CREATE TABLE IF NOT EXISTS Songs_collection(
	Song_id INT REFERENCES Songs(Song_id),
	Collection_id INT REFERENCES Collection(Collection_id),
	CONSTRAINT pk_songs_collection PRIMARY KEY (Song_id, Collection_id)
);