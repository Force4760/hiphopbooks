from . import replace
from typing import Any


def split(lyrics: str, separator: str = " ") -> list:
    """
    Function to split words into a list

    Parameters:
        lyrics (str): string of lyrics to be splitted
        separator (str): string that should separate each word
    Returns:
        (list): list of splitted words
    """
    return lyrics.strip().split(separator)


def remove_items(item_list: list, item: Any) -> list:
    """
    Function to remove (item) from a list

    Parameters:
        item_list (list): list in which items should be removed
        item (Any): anything that should be removed

    Returns:
        (list): list of filtered items
    """
    res = [i for i in item_list if i != item]
    return res


def separate(lyrics: str, toReplace: list) -> list:
    # replace provided patterns
    lyrics = replace(lyrics, toReplace=toReplace)
    # split lyrics into a list
    lyrics = split(lyrics, separator=" ")
    # remove null items from the list
    lyrics = remove_items(lyrics, "")
    return lyrics


def count(lyrics: str or list, toReplace: list = []) -> tuple:
    """
    Function to count words in a lyric

    Parameters
        lyrics (str or list): lyrics of a song, either as a string or a list of words.
        toReplace (list): list of regex patterns that should be replaced before counting a string

    Returns:
        (int): number of words in the lyrics
        (list): lyrics list. Each element is a word
    """
    if type(lyrics) == str:
        lyrics = separate(lyrics, toReplace)
    return len(lyrics), lyrics
