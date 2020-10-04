import sqlite3 # Import SQLite3

database = "art.sqlite3"

def create_artists_table():
    with sqlite3.connect("art.qlite3") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists (artist_name TEXT, artist_email TEXT (UNIQUE artist_email COLLATE NOCASE))")
    conn.close()

def create_artworks_table():
    with sqlite3.connect("art.qlite3") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artworks (artist_name TEXT, artwork_name TEXT, price REAL, available BOOLEAN (UNIQUE artwork_name COLLATE NOCASE))")
    conn.close()
