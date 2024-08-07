from lib.artist import Artist
from lib.album import Album

class ArtistRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by their id
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])
    
    def find_by_name(self, name):
        name = name.lower()
        rows = self._connection.execute(
            'SELECT * from artists WHERE lower(name) = %s', [name])
        try:
            row = rows[0]
        except IndexError:
            raise IndexError("Artist doesn't exist!")
        return Artist(row["id"], row["name"], row["genre"])
        
      
            
    
    def find_with_albums(self, artist_id):
        rows = self._connection.execute(
            "SELECT artists.id as artist_id, artists.name, artists.genre, albums.id AS album_id, albums.title, albums.release_year " \
            "FROM artists JOIN albums ON artists.id = albums.artist_id " \
            "WHERE artists.id = %s", [artist_id])
        albums = []
        for row in rows:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]["genre"], albums)
           
                
        

    # Create a new artist
    
    def create(self, artist):
        rows = self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        artist.id = rows[0]["id"]
        return None

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None
