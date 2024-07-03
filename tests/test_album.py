
from lib.album import Album
'''
When I construct an Album
With the fields id, title, release_year, artist_id
The fields are reflected in the instance properties
'''

def test_constructs_with_fields():
    album = Album(13, "Recto Verso", 2016, 6)
    assert album.id == 13
    assert album.title == "Recto Verso"
    assert album.release_year == 2016
    assert album.artist_id == 6
    
'''
When I construct two albums with the same fields
They are equal
'''
def test_equality():
    album_1 = Album(13, "Recto Verso", 2016, 6)
    album_2 = Album(13, "Recto Verso", 2016, 6)
    assert album_1 == album_2