import sqlite3 # Import SQLite3

database = "art.sqlite3"

def create_artist_table():
    with sqlite3.connect("art.qlite3") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists (artist_name TEXT, artist_email TEXT(UNIQUE artist_name COLLATE NOCASE, artist_email COLLATE NOCASE))")
    conn.close()
