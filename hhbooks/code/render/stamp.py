def render_stamp(to_write: str) -> str:
    """
    Function to render the stamp component

    Parameters:
        to_write (str): text to be written to the stamp.
            ideally it would be the name of the artist followed by the name of the album.

    Returns:
        (str): HTML for the stamp component
    """
    html = f"""
<div class="stamp">
  {to_write}
</div>
    """
    return html
