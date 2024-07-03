from playwright.sync_api import Page, expect


"""
When I GET /artists
We should get a list of artists back
"""

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Artist: Pixies\n Genre: Rock",
        "Artist: ABBA\n Genre: Pop",
        "Artist: Taylor Swift\n Genre: Pop",
        "Artist: Nina Simone\n Genre: Jazz"
        ])
"""
When I get artists/1
The artist with an ID of 1 should be returned (Pixies)
"""
    
def test_get_single_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Genre: Rock"
        ])
    
"""
When I GET /artists
We should get a list of artists back with a link to the artist page showing the artist info
"""

def test_get_artist_links_to_artist_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Artist: Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")
    
"""
When I add a new artist 
It should be added to the list of artists on the artists page
"""
def test_create_new_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add new artist'")
    
    page.fill("input[name=name]", "Test Artist")
    page.fill("input[name=genre]", "Rock")
    
    page.click("text='Add Artist'")
    
    page.goto(f"http://{test_web_address}/artists")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Artist: Pixies\nGenre: Rock",
        "Artist: ABBA\nGenre: Pop",
        "Artist: Taylor Swift\nGenre: Pop",
        "Artist: Nina Simone\nGenre: Jazz",
        "Artist: Test Artist\nGenre: Rock"
        ])
    
  
    