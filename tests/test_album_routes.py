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
    test_artist = page.get_by_test_id("t-artist")
    expect(test_artist).to_have_text("Artist: Pixies")
    test_release_year = page.get_by_test_id("t-release_year")
    expect(test_release_year).to_have_text("Release year: 1989")
    
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

def test_post_add_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/new")
    dropdown = page.locator("select.t-artist")
    page.fill("input[name=title]","Sugababes Covers")
    page.fill("input[name=release_year]","1990")
    dropdown.select_option("ABBA")
    add_album = page.get_by_role("button")
    add_album.click()
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sugababes Covers")
    test_artist = page.get_by_test_id("t-release_year")
    expect(test_artist).to_have_text("Release year: 1990")
    test_artist = page.get_by_test_id("t-artist")
    expect(test_artist).to_have_text("Artist: ABBA")
    