from .functions import render_css, render_html


def html_doc(css: str, html: str, name: str) -> str:
    doc = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>{css}</style>
    <link rel="stylesheet" href="../styles/global.css">
    <link rel="stylesheet" href="../styles/nav.css"
    <title>{name}</title>
</head>
<body>
    <nav>
        <a href="../index.html">Moleskin</a>
        <a class="nav-info" href="../info.html">Info</a>
    </nav>
    {html}
</body>
</html>
    """
    return doc


def render(link: str, songs_list: list, album: dict):
    name = album["name"]
    name = name.replace(" ", "")
    name = name.replace(".", "")
    name = name.replace(",", "")
    html = render_html(link, songs_list, album)
    css = render_css(album["image"])
    doc = html_doc(css, html, name)
    with open(name+".html", "w")as f:
        f.write(doc)
