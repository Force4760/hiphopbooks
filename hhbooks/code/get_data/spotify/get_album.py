import requests
from .auth import spotify_auth
import requests


def get_album(album_link: str, id_: str, secret: str, token_id: str) -> dict:
    """
    Function to get an album's info from the spotify api

    Parameters:
        album_link (str): link for the album (can be copied from the browser)
        id_ (str): client id from the spotify api
        secret (str): client secret/password from the spotify api
        token_id (str): url for the spotify api
    Returns:
        (dict): dictionary containing info on the album gathered from the spotify api
    """
    # get the album id from the album link
    # split link by / and get the last elemet
    # the last element is the id of the album
    album_id = album_link.rsplit('/', 1)[-1]

    # run auth function and get
    # the access_token and the time it expires in
    token = spotify_auth(id_, secret, token_id)

    # header for the spotify request
    header = {
        "Authorization": f"Bearer {token[0]}"
    }

    # format the endpoint, link + album id
    endpoint_link = f"https://api.spotify.com/v1/albums/{album_id}"

    # make the request to the spotify api
    r = requests.get(endpoint_link, headers=header)

    # check if the request was successful
    if r.status_code in range(200, 299):
        return r.json()
    else:
        raise Exception("The album request was not valid!")
