from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album
import pytest

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new ArtistRepository

    artists = repository.all() # Get all artists

    # Assert on the results
    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3)
    assert artist == Artist(3, "Taylor Swift", "Pop")

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "The Beatles", "Rock")
    repository.create(artist)
    assert artist.id == 5
    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "The Beatles", "Rock"),
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]
    

'''
When I call ArtistRepository #find_with_albums
The artist should be returned with their albums
'''

def test_find_with_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find_with_albums(1)
    assert artist == Artist(1, "Pixies", "Rock", [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Bossanova", 1990, 1),
    ])
    

'''
When I call ArtistRepository #find_by_name with an artist name
The artist with the matching name should be returned
'''

def test_find_artist_by_name(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find_by_name("ABBA")
    assert artist == Artist(2, "ABBA", "Pop")
    
'''
When I call ArtistRepository #find_by_name with an uppercase name
The artist with the matching name should be returned regardless of case
'''

def test_find_artist_by_name_check_case(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find_by_name("abba")
    assert artist == Artist(2, "ABBA", "Pop")
    
'''
When I call ArtistRepository #find_by_name with an artist that doesn't exist
I should get an error
'''

def test_find_artist_by_name_unknown_artist(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.find_by_name("someone")
    error_message = str(err.value)
    assert error_message == "Artist doesn't exist!"
    