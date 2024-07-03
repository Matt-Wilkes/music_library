from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
'''
When I call #all on the album repository
I get all of the albums back in a list
'''
def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,"Bossanova", 1990, 1),
        Album(4,'Voyage', 2023, 2)
        ]
    
'''
When I call #find on the album repository
I get the album back matching the id
'''

def test_find_returns_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find(1) == Album(1,'Doolittle', 1989, 1)
    
    
'''
When #create is called with an album
albums should update with the new user and email
'''

def test_new_album_created(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    album = Album(None,"Newest Album", 2024, 2)
    repository.create(album)
    assert album.id == 5
    assert repository.all() == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,"Bossanova", 1990, 1),
        Album(4,'Voyage', 2023, 2),
        Album(5,'Newest Album', 2024, 2),
        ]


'''
When #delete is called with an id
The album should be deleted from the albums table
'''

def test_album_deleted(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    repository.delete(2)
    assert repository.delete(2) is None
    assert repository.all() == [
        Album(1,'Doolittle', 1989, 1),
        Album(3,"Bossanova", 1990, 1),
        Album(4,'Voyage', 2023, 2)
        ]

# No longer needed 
# '''
# When I call #find on the album repository
# I get the album back matching the id
# '''

# def test_find_album_with_artist(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = AlbumRepository(db_connection)
#     assert repository.find_with_artist(1) == Album(1,'Doolittle', 1989, 1, [
#         Artist(1, 'Pixies', 'Rock')
#         ])
    