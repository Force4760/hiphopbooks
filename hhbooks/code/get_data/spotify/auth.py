import requests
import base64


def spotify_auth(client_id: str, client_secret: str, token_url: str) -> list:
    """
    Function to get the access_token and the time it expires from spotify

    Parameters:
        client_id (str): client id from the spotify api
        client_secret (str): client secret/password from the spotify api
        token_url (str): url for the spotify api
    Returns:
        (list): spotify access_token and the time (in ms) until it expires
    """
    # setup spotify creds
    client_creds = f"{client_id}:{client_secret}"
    # encode creds to base64
    client_creds_64 = base64.b64encode(client_creds.encode())

    token_data = {
        "grant_type": "client_credentials"
    }
    token_header = {
        "Authorization": f"Basic {client_creds_64.decode()}"
    }

    # make a request to spotify
    r = requests.post(token_url, data=token_data, headers=token_header)
    is_valid = r.status_code in range(200, 299)
    if is_valid:
        # get access_token and expire time
        response = r.json()
        access_token = response['access_token']
        expires_in = response['expires_in']
        return [access_token, expires_in]
    else:
        raise Exception("The request was not successful!")
