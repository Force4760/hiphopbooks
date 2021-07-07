import re


def replace(lyric: str, toReplace: list = [",", r"\.", r"\s+"]) -> str:
    """
    Function to replace multiple regex patterns from a string

    Parameters:
        lyric (str): lyrics of the song
        toReplace (list): list of regex patterns that should be replaced by ' '

    Returns:
        (str): lyrics with the patterns replaced
    """

    # replace ' from lyrics
    # since it can sometimes interfere with other functions
    lyric = re.sub("'", "", lyric)

    # replace all the other patterns
    for i in toReplace:
        lyric = re.sub(i, ' ', lyric)
    return lyric
