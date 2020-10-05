import sqlite3 # Import SQLite3
import main # Import main.py

database = "art.sqlite3" # For ease, make "database" a Global Variable always associated with "art.sqlite"

# Create Artists table function separately from Artworks table, if it doesn't already exist
def create_artists_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists (artist_name TEXT, artist_email BLOB)")
    conn.close()

# Create Artworks tale function separately from Artists table, if it doesn't already exist
def create_artworks_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artworks (artwork_name TEXT, artist_name TEXT, price REAL, available TEXT)")
    conn.close()

# Create tables
create_artists_table()
create_artworks_table()

# Using values from main.py update database with a new artist
def add_new_artist(new_artist_name, new_artist_email):
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artists VALUES (? , ?)", (new_artist_name , new_artist_email))
    conn.close()

# Using values from main.py update database with a new artwork
def add_new_artwork(new_artwork, new_artist, new_price, new_avaiability):
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artworks VALUES (? , ?, ?, ?)", (new_artwork, new_artist, new_price, new_avaiability))
    conn.close()

# Using values from main.py update database with the name of the artists whose artworks are to be displayed
def search_by_artist(search_artist):
    with sqlite3.connect(database) as conn:
        results = conn.execute("SELECT artwork_name FROM artworks WHERE artist_name like ?", (search_artist, ))
        return(results)
    conn.close()

# Using values from main.py update database with the name of the artwork to be deleted
def delete_artwork(deleted_artwork):
    with sqlite3.connect(database) as conn:
        conn.execute(f"DELETE FROM artworks WHERE artwork_name = ?", (deleted_artwork, ))
    conn.close()

# Using values from main.py update database with an artist's available artwork
def available_artwork(available_artist):
    with sqlite3.connect(database) as conn:
        results = conn.execute("SELECT artwork_name FROM artworks WHERE artist_name = ? AND available IS TRUE", (available_artist, ))
        return(results)
    conn.close()

