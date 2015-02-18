import unittest
import os

from main import generate_files, generate_output, get_sub_sequences

class OutputGenerationHelperTest(unittest.TestCase):

    def test_get_sub_sequences_empty(self):
        self.assertEqual(list(get_sub_sequences("")), [])

    def test_get_sub_sequences_short(self):
        self.assertEqual(list(get_sub_sequences("hi")), [])

    def test_get_sub_sequences_single(self):
        self.assertEqual(list(get_sub_sequences("cows")), ["cows"])

    def test_get_sub_sequences_multiple(self):
        """
        Tests decapitalization of letters, and non-skipping of repeat
        sequences.
        """
        self.assertEqual(list(get_sub_sequences("Mississippi")),
            ["miss", "issi", "ssis", "siss", "issi", "ssip", "sipp", "ippi"])

    def test_split_words(self):
        """
        Tests that numbers are not included in sequences, but do split
        sequences of letters.
        """
        self.assertEqual(list(get_sub_sequences("abc1defg2hijkl3")),
            ["defg", "hijk", "ijkl"])

class OutputGenerationTest(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(set(generate_output([])), set([]))

    def test_single_word(self):
        """
        Tests decapitalization of letters, and non-exclusion of repeat
        sequences within one word. NOTE: Requirements specified
        excluding sequences repeated *in multiple words*, not repeated
        within words.
        """
        self.assertEqual(set(generate_output(["Mississippi"])), {
            ("ippi", "Mississippi"),
            ("issi", "Mississippi"),
            ("miss", "Mississippi"),
            ("sipp", "Mississippi"),
            ("siss", "Mississippi"),
            ("ssip", "Mississippi"),
            ("ssis", "Mississippi"),
        })

    def test_sequenc_collision(self):
        """
        Tests case-insensitive removal of sequences that appear in
        multiple words.
        """
        self.assertEqual(set(generate_output(["Anthony", "anthem"])), {
            ("ntho", "Anthony"),
            ("thon", "Anthony"),
            ("hony", "Anthony"),
            ("nthe", "anthem"),
            ("them", "anthem"),
        })

class FileGenerationTest(unittest.TestCase):
    # For simplicity, limit the amount of I/O based tests.
    # For other tests we can use output generation functions.

    # Filenames unlikely to be in use for other things, to avoid sadness
    # when deleting
    SEQUENCES_FNAME = "test_sequences.784971024.tmp"
    WORDS_FNAME = "test_words.7473219.tmp"
    INPUT_FNAME = "test_input.8932842.tmp"

    def _delete_files(self):
        for fname in [self.SEQUENCES_FNAME, self.WORDS_FNAME, self.INPUT_FNAME]:
            if os.path.exists(fname):
                os.remove(fname)

    def setUp(self):
        # Make sure the expected files don't exist yet
        self._delete_files()

    def test_files_created(self):
        """
        Tests that output files are generated.
        """
        self.assertFalse(os.path.exists(self.SEQUENCES_FNAME))
        self.assertFalse(os.path.exists(self.WORDS_FNAME))
        self.assertFalse(os.path.exists(self.INPUT_FNAME))

        with open(self.INPUT_FNAME, "w") as input_f:
            input_f.write("Anthony\nanthem")

        success, msg = generate_files(input_fname=self.INPUT_FNAME,
                                    sequences_fname=self.SEQUENCES_FNAME,
                                    words_fname=self.WORDS_FNAME)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(self.SEQUENCES_FNAME))
        self.assertTrue(os.path.exists(self.WORDS_FNAME))

        with open(self.SEQUENCES_FNAME, "r") as sequences_f, open(self.WORDS_FNAME, "r") as words_f:
            sequences = sequences_f.read().split("\n")
            words = words_f.read().split("\n")

        self.assertEqual(set(zip(sequences, words)), {
            ("ntho", "Anthony"),
            ("thon", "Anthony"),
            ("hony", "Anthony"),
            ("nthe", "anthem"),
            ("them", "anthem"),
        })

    def test_missing_file(self):
        self.assertFalse(os.path.exists(self.INPUT_FNAME))

        success, msg = generate_files(input_fname=self.INPUT_FNAME,
                              sequences_fname=self.SEQUENCES_FNAME,
                              words_fname=self.WORDS_FNAME)

        self.assertFalse(success)
        self.assertTrue("no such file" in msg.lower(), msg)

    def tearDown(self):
        # So as not to leave a mess
        self._delete_files()

if __name__ == '__main__':
    unittest.main()
