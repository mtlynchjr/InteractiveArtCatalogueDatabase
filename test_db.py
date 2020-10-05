import sqlite3
import db
from db import database
import unittest
from unittest import TestCase

class TestArtDatabase(TestCase):
    test_database = "test_art.sqlite3"
    
    # Set-up test database and clone of actual database. Empty database.
    def setUp(self):
        db.database = self.test_database
        with sqlite3.connect(self.test_database) as conn:
            conn.execute("DELETE FROM artists")
            conn.execute("DELETE FROM artworks")
        conn.close()
    
    # Create test values for adding a new artist and add to test database
    def test_add_new_artist(self):
        db.add_new_artist("Pablo Picasso", "pp@aol.com")
        expected = {"Pablo Picasso" : "pp@aol.com"}
        self.compare_db_to_expected(expected)

    # Create test values for adding a new artwork and add to test database
    def test_add_new_artwork(self):
        db.add_new_artwork("Starry Night", "Vincent Van Gogh", 1000, "no")
        expected ={"Starry Night" : "Vincent Van Gogh" : 1000 : "no"}
        self.compare_db_to_expected(expected)

    # Create a test value for selecting a specific artist from the test database
    def test_search_by_artist(self):
        db.search_by_artist("Winslow Homer")
        expected = {"Winslow Homer"}
        self.compare_db_to_expected(expected)

    # Create a test value to for finding and deleting an artwork from the test database
    def test_delete_artwork(self):
        db.delete_artwork("Nighthawks")
        expected = {"Nighthawks"}
        self.compare_db_to_expected(expected)

    # Create a test value for finding an artwork in the test databse to determine its availability
    def test_available_artwork(self):
        db.available_artwork("American Gothic")
        expected ={"American Gothic"}
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
