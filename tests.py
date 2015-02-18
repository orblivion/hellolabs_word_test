import unittest
import os

from main import generate_files, generate_output, get_sub_sequences

class FileGenerationTest(unittest.TestCase):
    def setUp(self):
        # Make sure the expected files don't exist yet
        for fname in ["test_sequences", "test_words"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_files_created(self):
        """
        Tests that output files are generated.
        """
        # For simplicity this will be the only I/O based test.
        # For other tests we can use output generation functions.

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

class OutputGenerationHelperTest(unittest.TestCase):

    def test_get_sub_sequences_empty(self):
        self.assertEqual(list(get_sub_sequences("")), [])

    def test_get_sub_sequences_short(self):
        self.assertEqual(list(get_sub_sequences("hi")), [])

    def test_get_sub_sequences_single(self):
        self.assertEqual(list(get_sub_sequences("cows")), ["cows"])

    def test_get_sub_sequences_multiple(self):
        # Tests decapitalization of letters, and non-skipping of repeat sequences
        expected_output = ["miss", "issi", "ssis", "siss", "issi", "ssip", "sipp", "ippi"]
        self.assertEqual(list(get_sub_sequences("Mississippi")), expected_output)

class OutputGenerationTest(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(generate_output([]), set([]))

if __name__ == '__main__':
    unittest.main()
