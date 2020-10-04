import sqlite3 # Import SQLite3

database = "art.sqlite3" # For ease, make "database" a Global Variable always associated with "art.sqlite"

def create_artists_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists (artist_name TEXT, artist_email TEXT)")
    conn.close()

def create_artworks_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artworks (artwork_name TEXT, artist_name TEXT, price REAL, available BOOLEAN)")
    conn.close()

def add_new_artist():
    new_artist_name = input("What is the name of the artist you would like to add? ") # Prompt useer for new artist's name
    new_artist_email = input("Please enter the e-mail address of the artist you would like to add: ") # Prompt user for new artist's e-mail address
    
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artists VALUES (? , ?)", (new_artist_name , new_artist_email))
    conn.close()

def add_new_artwork():
    new_artwork = input("What is the name of the artwork you would like to add? ") # Prompt user for new artworks's name
    new_artist = input("What is the name of the artist attributed to that artwork? ") # Prompt user for new artwork's artist
    new_price = float(input("How much does the artwork cost? $")) # Prompt user for new artwork's price.
    new_avaiability = input("Is the artwork currently available for purchase? ") # Prompt user for new artwork's availability
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artworks VALUES (? , ?, ?, ?)", (new_artwork, new_artist, new_price, new_avaiability))
    conn.close()

def delete_artwork():
    delete_artwork = input("What is the name of the artwork you would like to remove? ")
    with sqlite3.connect(database) as conn:
        conn.execute(f"DELETE FROM artworks WHERE artwork_name = ?", (delete_artwork, ))
    conn.close()

create_artists_table()
create_artworks_table()
add_new_artist()
add_new_artwork()
delete_artwork()
