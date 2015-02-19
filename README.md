This program will take a list of words and produce two output lists. The first output list will contain every four-letter sequence that appears in exactly one word of the input list (though it can appear twice in a given word). The second output list will contain the list of words that correspond, in order, to each sequence in the first list. As such, the second list will likely contain repeated words.

Sequences are case insensitive. Non-letter characters are not included in sequences. Numbers in particular will interrupt sequences of letters. Non-alphanumeric characters will not.

For example, for the word `abc7dE-fgh`, `defg` and `efgh` are the only valid sequences.

The sequences output in the first list are all lower case, and do not include non-letter characters. However, the corresponding words in the other output list maintain their original formatting.

To use the program, put the input list in a file. The output will appear in two separate files.

# Installation

Designed for Ubuntu. This has no pip dependencies. Just clone the repository:

    $ git clone ...

(Replace the URL with the appropriate URL if you're looking at a fork or copy hosted elsewhere.)

# Testing

    $ python tests.py 

You should get:

    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.001s

    OK

Note that tests create and delete files in the current working directory.

# Running

To see detailed instructions:

    ./main.py --help

To run:

    ./main.py input_filename sequences_filename words_filename
