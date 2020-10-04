import sqlite3 # Import SQLite3

database = "art.sqlite3" # For ease, make "database" a Global Variable always associated with "art.sqlite"

def create_artists_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists (artist_name TEXT, artist_email TEXT (UNIQUE artist_email COLLATE NOCASE))")
    conn.close()

def create_artworks_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artworks (artist_name TEXT, artwork_name TEXT, price REAL, available BOOLEAN (UNIQUE artwork_name COLLATE NOCASE))")
    conn.close()

def add_new_artist():
    new_artist_name = input("What is the name of the artist you would like to add? ") # Prompt useer for new artist's name
    new_artist_email = input("Please enter the e-mail address of the artist you would like to add: ") # Prompt user for new artist's e-mail address
    
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artists VALUES (? , ?)", (new_artist_name , new_artist_email))
    conn.close()


