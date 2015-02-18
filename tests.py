import unittest
import os

from main import generate_files

class WordsTest(unittest.TestCase):
    def setUp(self):
        # Make sure the expected files don't exist yet
        for fname in ["test_sequences", "test_words"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_files_created(self):
        self.assertFalse(os.path.exists("test_sequences"))
        self.assertFalse(os.path.exists("test_words"))
        generate_files([], sequences_fname="test_sequences", words_fname="test_words")
        self.assertTrue(os.path.exists("test_sequences"))
        self.assertTrue(os.path.exists("test_words"))

    def tearDown(self):
        # So as not to leave a mess
        for fname in ["test_sequences", "test_words"]:
            if os.path.exists(fname):
                os.remove(fname)

if __name__ == '__main__':
    unittest.main()
