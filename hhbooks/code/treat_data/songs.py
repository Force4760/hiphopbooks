# write docstring
from . import count
import re


def songs(spotify: dict, genius: list) -> list:
    """
    Function to join spotify and genius data into usable data.

    Parameters:
        spotify (dict): dict containing album and track data from spotify.
        genius (list): list containing album and track data from genius
    Returns:
        (list): list containing several dicts, one for each track
    """

    # spotify data
    tracks_sp = spotify["tracks"]

    # list with track info
    finalTracks = []
    for i in range(len(tracks_sp)):
        # process the artists that made this track
        artists = []
        for a in tracks_sp[i]["artists"]:
            artists.append(a["name"])

        # get track lyrics from genius data
        lyrics = genius[i]["song"]["lyrics"]

        # count words and separate lyrics
        word_count, lyrics = count(
            lyrics, [r"\[.*\]", r"\?", ",", r"\.", r"\s+", "'", "EmbedShare", "Url:CopyEmbed:Copy", ":", r"\(", r"\)", "}", "{"])

        name = re.sub(r"(\(.*\))", "", tracks_sp[i]["name"])
        # info for this track
        # name, number, time, lyrics, count and artists
        info = {
            "name": name,
            "number": genius[i]["number"],
            "time": tracks_sp[i]["duration_ms"],
            "lyrics": lyrics,
            "word_count": word_count,
            "artists": artists
        }

        # add this track to the final list
        finalTracks.append(info)
    return finalTracks
