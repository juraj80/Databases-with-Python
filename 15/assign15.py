import sqlite3

conn=sqlite3.connect('trackdb.sqlite')
cur=conn.cursor()

cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
for row in cur:
	print row

conn.close()

