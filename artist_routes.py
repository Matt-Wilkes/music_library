from lib.database_connection import get_flask_database_connection
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import request, render_template, redirect, url_for

def apply_artist_routes(app):
    @app.route('/artists', methods=["GET"])
    def get_artists():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        artists = repository.all()
        return render_template('artists/artists.html', artists=artists)
    
    @app.route('/artists/<id>',methods=["GET"])
    def get_artist_by_id(id):
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        artist = repository.find(id)
        return render_template('artists/artist_page.html', artist=artist)
    
    @app.route('/artists/new', methods=["GET"])
    def get_artist_new():
        return render_template('artists/new.html')
    
    @app.route('/artists', methods=["POST"])
    def post_new_artist():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        name = request.form['name']
        genre = request.form['genre']
        
        artist = Artist(None, name, genre)
        repository.create(artist)
        return redirect(f"/artists/{artist.id}")