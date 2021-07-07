def render_player(album: dict, link: str) -> str:
    """
    Function to render the album player component

    Parameters:
        album (dict): dict containing info on the album
        link (str): link to the album, so that it is opened when the player is pressed
    Returns:
        (str): final HTML for the player component
    """

    # get selected info from the album dict
    image = album["image"]
    name = album["name"]

    # final HTML for the player
    html = f"""
<div class="artist">
<a href="{link}" target="_blank" class="songlink" >
<div class="player">
  <img src="{image}" alt="album" class="playerart">
   <span class="play">
        <span class="songname"> <strong > {name} </strong> </br > </span>
        <span>« ▷ »</span>
    </span>
</div>
</a>
</div>
    """
    return html
