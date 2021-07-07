def render_info(data: dict) -> str:
    """
    Function to render the info page

    Parameters:
        data (dict): a dict with the album info

    Returns:
        (str): final HTML for the info page
    """

    # get and treat info from the data dict
    name = data["name"]
    artists = ",".join(data["artists"])
    date = data["date"]
    date = date.replace("-", "/")
    label = data["label"]
    art = data["image"]

    # render components of the info page
    album_str = render_album(name)
    artist_str = render_artist(artists)
    date_str = render_date(date)
    label_str = render_label(label)
    cover_str = render_cover(
        art, "https://cdn140.picsart.com/305125781110211.png?r1024x1024")

    # final html for the info
    html = f"""
<div class="info">
    {album_str}
    {artist_str}
    {date_str}
    {label_str}
</div>
{cover_str}
    """
    return html


def render_album(name: str) -> str:
    """
    Function to render the album name part of the info

    Parameters:
        name (str): name of the album

    Returns:
        (str): html for the album name
    """
    return f"<p><strong>Album :</strong> {name}</p>"


def render_artist(name: str) -> str:
    """
    Function to render the artist name part of the info

    Parameters:
        name (str): name of the artist

    Returns:
        (str): html for the artist name
    """
    return f"<p><strong>Artist :</strong> {name}</p>"


def render_date(date: str) -> str:
    """
    Function to render the release date part of the info

    Parameters:
        date (str): release date of the album

    Returns:
        (str): html for the release date
    """
    return f"<p><strong>Date :</strong> {date}</p>"


def render_label(label: str) -> str:
    """
    Function to render the label part of the info

    Parameters:
        label (str): name of the label of the album

    Returns:
        (str): html for the label
    """
    return f"<p><strong>Label :</strong> {label}</p>"


def render_cover(image: str, tape: str) -> str:
    """
    Function to render the cover image part of the info

    Parameters:
        image (str): link to the album cover image
        tape (str): link to the tape that holds the cover

    Returns:
        (str): html for the cover
    """
    html = f"""
<div class="cover">
<img src="{image}" alt = "album art" class="picture"/>
<img src="{tape}" alt = "tape" class="tape1 top"/>
<img src="{tape}" alt = "tape" class="tape1 bottom"/>
</div>
    """
    return html
