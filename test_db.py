import sqlite3
import unittest
from unittest import TestCase
import db
from db import database

class TestArtDatabase(TestCase):
    test_database = "test_art.sqlite3"
    
    def setUp(self):
        db.database = self.test_database
        with sqlite3.connect(self.test_database) as conn:
            conn.execute("DELETE FROM artists")
            conn.execute("DELETE FROM artworks")
        conn.close()
   
    def test_add_new_artist(self):
        db.add_new_artist("Pablo Picasso", "pp@aol.com")
        expected = {"Pablo Picasso" : "pp@aol.com"}
        self.compare_db_to_expected(expected)

        db.add_new_artist("Winslow Homer", "winsdoh@gmail.com")
        expected = {"Winslow Homer" : "winsdoh@gmail.com"}
        self.compare_db_to_expected(expected)

        def compare_db_to_expected(self, expected):

            conn = sqlite3.connect(self.test_database)
            cursor = conn.cursor()
            all_data = cursor.execute("SELECT * FROM database").fetchall()

            self.assertEqual(len(expected.keys()), len(all_data))

            for row in all_data:
                self.assertsIn(row[0], expected.keys())
                self.assertEqual(expected[row[0]], row[1])
            
            conn.close()

if __name__ == "__main__":
    unittest.main()
