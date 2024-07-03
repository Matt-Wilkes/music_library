from playwright.sync_api import Page, expect
import pytest

"""
When I GET /albums
We should get a list of albums back
"""

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988",
        "Title: Bossanova\nReleased: 1990",
        "Title: Voyage\nReleased: 2023"
        ])
"""
When I get albums/1
The album with an ID of 1 should be returned
"""
    
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Release year: 1989\nArtist: Pixies"
        ])
    
"""
When I GET /albums
We should get a list of albums back with a link to the album
"""

def test_get_albums_links(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Title: Doolittle'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")
    
"""
When I get albums/new
'Artist' should show a dropdown with the current artists
"""
def test_get_new_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/new")
    dropdown = page.locator("select.t-artist")
    options = dropdown.locator('option')
    expect(options).to_have_text(['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone'])
    
"""
When I add a new album
The album should be displayed on the album_page
"""
@pytest.mark.skip(reason ="need to test artist repository functionality test first")
def test_post_add_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/new")
    page.fill("input[name=title]","New album")
    page.fill("input[name=release_year]","1990")
    page.fill("input[name=artist]","Artist")
    page.click("text=Add Album")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("New album")
    