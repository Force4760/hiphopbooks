def more_used(text: list) -> tuple:
    """
  Parameters:
    text (list): text in which to count the words in list form (one element per word)
  Returns:
    (list): list of the words sorted from the most used to the least used.
    (int): total number of words.
    """

    # total number of words
    number = 0

    # dict with the words
    counted_words = {}

    # loop trough every word
    for word in text:
        if word not in counted_words:
            # add the word to the dict
            counted_words[word.lower()] = 1
        else:
            # update the count of the specified word
            counted_words[word] += 1
        number += 1

    # sort counted words by the
    # number of times a word is used
    sort = sorted(counted_words.items(),
                  key=lambda item: item[1], reverse=True)
    return sort, number
