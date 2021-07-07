from .get_album import get_album
from .auth import spotify_auth


def album_info(link: str, id_: str, secret: str, token: str) -> dict:
    """
    Function to connect and retrieve data from the spotify api about a specific album

    Parameters:
        link (str): link to the album
        (can be obtained by copying the link from the spotify page)
        id_ (str): client id from the spotify api
        secret (str): client secret/password from the spotify api
        token (str): url for the spotify api
    Returns:
        (dict): dictionary containing an album's info.
        name, artists, data, label, image and a list of track dicts
    """

    # connect to the spotify api
    # and get info on the album
    album = get_album(link, id_, secret, token)

    # album name
    name = album["name"]

    # process album artists
    artists = artists_list(album["artists"])

    # release date for the album
    date = album["release_date"]

    # label that released the album
    label = album["label"]

    # list of tracks and info on them
    tracks = album["tracks"]["items"]

    # cover image for the album
    image = album["images"][0]["url"]

    # final album info dict
    info = {
        "name": name,
        "artists": artists,
        "date": date,
        "label": label,
        "image": image,
        "tracks": tracks
    }
    return info


def artists_list(artists_dict: dict) -> list:
    """
    Function to format the artists name from
    the data retrieved from the spotify api

    Parameters:
        artists_dict (dict): dictionary, retrieved from the spotify api,
        that contains info on the artists of a certain album
    Returns:
        (list): a list containing the names of every main artist
        on a certain album
    """
    artists = []

    # add the name of every artist
    for a in artists_dict:
        artists.append(a["name"])
    return artists
