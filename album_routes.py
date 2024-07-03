from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import request, render_template, redirect, url_for

def apply_album_routes(app):
    @app.route('/albums', methods=["GET"])
    def get_albums():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        albums = repository.all()
        return render_template('albums/albums.html', albums=albums)

    @app.route('/albums/<id>', methods=["GET"])
    def get_album(id):
        connection = get_flask_database_connection(app)
        album_repository = AlbumRepository(connection)
        artist_repository = ArtistRepository(connection)
        album = album_repository.find(id)
        artist = artist_repository.find(album.artist_id)
        return render_template('albums/album_page.html', album=album, artist=artist)

    @app.route('/albums/new', methods=["GET"])
    def get_album_new():
        return render_template('albums/new.html')
    
    # Not working :(
    @app.route('/albums', methods=["POST"])
    def post_new_album():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        title = request.form['title']
        print(title)
        release_year = int(request.form['release_year'])
        print(release_year)
        artist = request.form['artist']
        id = Artist.find_by_name(artist)
        album = Album(None, title, release_year, id)
        repository.create(album)
        return redirect(f"/albums/{album.id}")

    
