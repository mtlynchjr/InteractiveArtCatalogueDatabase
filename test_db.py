import sqlite3
import unittest
from unittest import TestCase
import db
from db import database

class TestArtDatabase(TestCase):
    test_database = "test_art.sqlite3"
    
    # Set-up test database and clone of actual database. Empty database.
    def setUp(self):
        db.database = self.test_database
        with sqlite3.connect(self.test_database) as conn:
            conn.execute("DELETE FROM artists")
            conn.execute("DELETE FROM artworks")
        conn.close()
    
    # Create values to be inputted and confirm that they function correctly
    def test_add_new_artist(self):
        db.add_new_artist("Pablo Picasso", "pp@aol.com")
        expected = {"Pablo Picasso" : "pp@aol.com"}
        self.compare_db_to_expected(expected)

    # Create values to be inputted and confirm that they function correctly
    def test_add_new_artwork(self):
        db.add_new_artwork("Starry Night", "Vincent Van Gogh", 1000, "no")
        expected ={"Starry Night", "Vincent Van Gogh", 1000, "no"}
        self.compare_db_to_expected(expected)

    # Create values to be inputted and confirm that they function correctly
    def test_search_by_artist(self):
        db.search_by_artist("Winslow Homer")
        expected = {"Winslow Homer"}
        self.compare_db_to_expected(expected)

    # Create values to be inputted and confirm that they function correctly
    def test_delete_artwork(self):
        db.delete_artwork("Nighthawks")
        expected = {"Nighthawks"}
        self.compare_db_to_expected(expected)

    # Create values to be inputted and confirm that they function correctly
    def test_available_artwork(self):
        db.available_artwork("Georgia O'Keefe")
        expected ={"Georgia O'Keefe"}
        self.compare_db_to_expected(expected)

    # From unit testing video lecture "compare to expected" created for ease
    def compare_db_to_expected(self, expected):
        conn = sqlite3.connect(self.test_database)
        cursor = conn.cursor()
        all_data = cursor.execute("SELECT * FROM database").fetchall()

        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            self.assertEqual(expected[row[0]], row[1])

        conn.close()

# Call main function
if __name__ == "__main__":
    unittest.main()
    