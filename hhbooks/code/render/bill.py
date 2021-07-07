from ..treat_data import millis_to_min_str


def render_head(columns: list = ["Tracks", "Time", "Words"]) -> str:
    """
    Function to render the header of the bill table

    Parameters:
        columns (list): a list of strings to be used a table header titles

    Returns:
        (str): final HTML for the header of the bill table
    """

    # rendering the titles
    inner = ""
    for column_name in columns:
        inner += f"<th>{column_name}</th>"

    # rendering the final header html
    html = f"""
    <thead>
        <tr>
            {inner}
        </tr>
    </thead>
    """
    return html


def render_body(tracks: list) -> tuple:
    """
    Function to render the header of the bill table

    Parameters:
        tracks (list): list of dict tracks. Each dict holds info on a track (like the name, time, lyrics...)

    Returns:
        (str): final HTML for the header of the bill table
        (list): list containing the totals that will be used in the footer
    """

    # total number of tracks
    total_number = 0
    # total time/length of the tracks
    total_time = 0
    # total count of words
    total_words = 0

    # rendering the inner HTML for the body
    inner = ""
    for track in tracks:
        # name of the track
        name = track["name"]
        # time of the track
        time = track["time"]
        # number of words of the track
        words = track["word_count"]

        # update totals
        total_number += 1
        total_time += time
        total_words += words

        # data/line for each song
        data = f"<td>{name}</td>"
        data += f"<td>{millis_to_min_str(time)}</td>"
        data += f"<td>{words}</td>"

        # update inner HTML
        inner += f"<tr>{data}</tr>"

    # render final body html
    html = f"""
    <tbody>
        {inner}
    </tbody>
    """
    return html, [total_number, millis_to_min_str(total_time), total_words]


def render_footer(totals: list) -> str:
    """
    Function to render the footer of the bill table

    Parameters:
        totals (list): a list of values to be printed in a footer

    Returns:
        (str): final HTML for the footer of the bill table
    """

    # creating the table data for the footer
    inner = ""
    for total_value in totals:
        inner += f"<td>{total_value}</td>"

    # creating the divider between the body and the footer
    divider = "<td> Total </td>"
    for _ in range(len(totals)-1):
        divider += f"<td> ----- </td>"

    # render the final footer
    html = f"""
    <tr class = "total">
        {divider}
    </tr>
    <tfoot>
       <tr>
            {inner}
        </tr>
    </tfoot>
    """
    return html


def render_bill(tracks: list, columns: list = ["Tracks", "Time", "Words"]):
    """
    Function to render the "bill".
    bill is a table that ocupies one full page

    Parameters:
        tracks (list): list of dict tracks. Each dict holds info on a track (like the name, time, lyrics...)
        columns (list): list of the name for the columns
    Returns:
        (str): HTML string of the bill table
    """

    # rendering the table header
    head_str = render_head(columns)

    # rendering the body of the table
    # body_str is the HTML body
    # totals is a list of the sums for the footer
    body_str, totals = render_body(tracks)

    # rendering the footer of the table
    footer_str = render_footer(totals)

    # final HTML for the table
    html = f"""
    <table class = "bill">
        {head_str}
        {body_str}
        {footer_str}
    </table>
    """
    return html
