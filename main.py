def generate_files(dictionary, sequences_fname="sequences", words_fname="words"):
    open(sequences_fname, "w")
    open(words_fname, "w")

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
    if not dictionary: return set([])
    word = dictionary[0]
    for sequence in get_sub_sequences(word):
        sequence_record[sequence] = word
    return set(sequence_record.iteritems())
