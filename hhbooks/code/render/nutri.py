from ..treat_data import more_used


def render_nutri(songs: list) -> tuple:
    """
    Function to render the final HTML of the nutrition table

    Parameters:
        songs (list): a list containg song dicts

    Returns:
        (str): final html for the nutrition table
        (list): list of the top 5 most used words
    """

    # join all words from every lyric into a single list
    lyrics = []
    for song in songs:
        lyrics += song["lyrics"]

    # sort all words
    words, _ = more_used(lyrics)

    # get the top 5 words
    data = top_x(words, 5)

    # render all the lines of the table
    inner = ""
    for i in range(len(data)):
        inner += nutri_line(data[i][0], data[i][1], f"m{i+1}")

    # final html for the nutrition table
    html = f"""
<table class="nutrition">
    <thead>
        <tr>
            <th>Words</th>
            <th>Number</th>
        </tr>
    </thead>
    <tbody>
        {inner}
    </tbody>
</table>
    """
    return html, data


def top_x(sorted_words: list, x: int) -> list:
    """
    Function to return the X most used words

    Parameters:
        sorted_words (list): a list of all the words in the album sorted by the number of times they are used
        x (int): the number of words to return

    Returns:
        (list): list containg X words. Each word is a list of the type [word, number]
    """

    # init final list
    final = []

    # see new words until X are chosen
    i = 0
    while len(final) < x:
        # get word from sorted_words
        word = sorted_words[i][0]
        # get number from sorted_words
        number = sorted_words[i][1]

        # ask user if they want to consider this word
        answer = input(f"Do you want to consider {word} ({number}): ")
        if answer.lower() == "y" or answer.lower() == "yes":
            # add this word to the final list
            final.append([word, number])
        i += 1

    return final


def nutri_line(word: str, number: int, mark_class: str) -> str:
    """
    Function to create each line of the nutrition table

    Parameters:
        word (str): the word to render
        number (int): the number of times the word is used
        mark_class (str): the class to be used for styling purposes

    Returns:
        (str): HTML for the line
    """
    line = f"""
    <tr>
        <td><mark class="{mark_class}">{word.capitalize()}</mark></td>
        <td class="percentage">{number}</td>
    </tr>
    """
    return line
