def render_colabs(tracks: list, main_artists: list) -> str:
    """
    Function to render the html for the colabs component

    Parameters:
        tracks (list): list of dicts conatining info on each track
        main_artists (list): list of all main artists in the album

    Returns:
        (str): HTML for the colabs component
    """
    # get all colabs
    colabs = process_colabs(tracks, main_artists)
    # turn colabs into an HTML list
    html_list = colabs_list(colabs)
    # final HTML
    html = f"""
<div class = "info2" >
    <ul>
        <li> <strong> Colabs: </strong></li>
        {html_list}
    </ul>
</div>
    """
    return html


def colabs_list(colabs: list) -> str:
    """
    Generate an html list from the info on the colabs in the album

    Parameter:
        colabs (list): list containing all colaboration in the album
            Artist - track name
    Returns:
        (str): html list with a <li> tag for each colab
    """
    html = ""
    for artist in colabs:
        # create a new list item
        # and format the info to a title
        html += f"<li>{artist.title()}</li>"
    return html


def process_colabs(tracks: list, main_artists: list) -> list:
    """
    Function to process the colabs in an album

    Parameters:
        tracks (list): list of dicts conatining info on each track
        main_artists (list): list of all main artists in the album

    Returns:
        (list): list of colabs in the album
    """
    colabs = []
    for track in tracks:
        # get all colabs in this track
        colabs = get_all_artists(
            track["artists"], track["name"], colabs, main_artists)
    return colabs


def get_all_artists(artists: list, track_name: str, colabs: list, main_artists: list) -> list:
    """
    Function to get all colabs in this track

    Parameters:
        artists (list): list of artists
        track_name (str): name of this track
        colabs (list): list containing previously added colabs
        main_artists (list): list containing the main artists for this album

    Returns:
        (list): colabs list with all the added colabs
    """
    for artist in artists:
        # check if the artist is a colab
        # not the main artist
        if artist not in main_artists:
            # format artist as ArtistName - TrackName
            artist = artist + " - " + track_name
            # check if this colab is not repeated
            colabs = check_artist(artist, colabs)
    return colabs


def check_artist(artist: str, colabs: list) -> list:
    """
    Function to check if the provided artist is not already in colabs

    Parameter:
        artist (str): current artist to be checked
        colabs (list): list of previously added colabs
    Returns:
        (list): colab with artist if it was not already there
    """
    # add asrtist if it is not
    # already in the colabs list
    if artist not in colabs:
        colabs.append(artist)
    return colabs
