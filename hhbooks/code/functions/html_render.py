from ..render import render_bill, render_info, render_nutri, render_player, render_colabs, render_quotes


def render_html(link: str, songs_list: list, album: dict) -> str:
    bill = render_bill(songs_list)
    info = render_info(album)
    nutri, data = render_nutri(songs_list)
    player = render_player(album, link)
    colabs = render_colabs(songs_list, album["artists"])
    quotes = render_quotes(2, data)
    html = f"""
<div class="moleskine-wrapper">
    <div class="moleskine-notebook">
        <input type="checkbox" id="btn"></input>
        <div class="notebook-cover">
            <div class="notebook-skin">
                <div class="text">
                    {album["name"]}
                    <br/>
                    {",".join(album["artists"])}
                </div>
            </div>
        </div>

        <div class="notebook-page dotted"></div>
        <div class="page notebook-page dotted"></div>
        <div class="page2 notebook-page dotted"></div>
        {bill}
        {nutri}
        {info}
        {quotes}
        {colabs}
        {player}
    </div>
</div>
    """
    return html
