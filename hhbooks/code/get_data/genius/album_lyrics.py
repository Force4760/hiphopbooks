from lyricsgenius import Genius
import json


def get_album_lyrics(token: str, name: str, artist: list) -> list:
    """
    Function to connect and retrieve album data and lyrics from genius.
    Parameters:
        token (str): token string to autenticate the connection to the genius API.
        name (str): name of the album you want to search for
        artist (list): list containing the name of every main artist

    Returns:
        track (list): a list containing one dictionary for every song on the album. The lyrics are contained within the dict for each song.
    """
    #
    artists_name = " ".join(artist)
    # connect to the genius API
    genius = Genius(token, timeout=120)

    while True:
        # search for the requested album
        album = genius.search_album(name, artists_name)
        try:
            # convert album to a python dictionary
            album = album.to_dict()
        except:
            print("Sorry. We couldn't find this album")
            yes = input("Do you want to try a new name/artist? (y/n) ")
            if yes.lower() == "yes" or yes.lower() == "y":
                name = input("Album Name: ")
                artists_name = input("Artist(s) Name(s): ")
                continue
        break
    # return the tracks info as a list of dicts
    return album["tracks"]
