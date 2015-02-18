def generate_files(input_fname, sequences_fname, words_fname):
    try:
        with open(input_fname, "r") as input_f:
            input_words = [line.strip() for line in input_f]
    except IOError as e:
        return False, str(e)

    sequences, words = zip(*generate_output(input_words))

    with open(sequences_fname, "w") as sequences_f:
        sequences_f.write("\n".join(sequences))
    with open(words_fname, "w") as words_f:
        words_f.write("\n".join(words))

    return True, None

def get_sub_sequences(word):
    """
    Take a word, and yield all four letter sequences, lower cased.
    """
    # Create offset versions of the word.
    # Ex: "general" -> ["general", "eneral", "neral", "eral"]
    offset_words = [word[offset_index:] for offset_index in range(4)]

    # Now we can line them up with zip, and look across them for four
    # letter sequences of the original word
    for offset_letters in zip(*offset_words):
        # zip gives tuples. make `offset_letters` back into a string, lower case
        yield "".join(offset_letters).lower()

def generate_output(dictionary):
    sequence_record = {}
    for word in dictionary:
        for sequence in get_sub_sequences(word):
            if sequence not in sequence_record:
                # It's a new sequence. Include it until further notice
                sequence_record[sequence] = word
            elif sequence_record[sequence] != word:
                # It's a repeated sequence. It was in a different word,
                # or was already excluded. Exclude it.
                sequence_record[sequence] = None
    for sequence, word in sequence_record.iteritems():
        if word is not None:
            yield sequence, word
