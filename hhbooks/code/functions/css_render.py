from .colors import main_colors


def render_css(art: str) -> str:
    dark, light, skin = main_colors(art)
    cover = f"--cover: rgb({light[0]}, {light[1]}, {light[2]});"
    cover += f"--coverDark: rgb({dark[0]}, {dark[1]}, {dark[2]});"
    cover += f"--skinLine: rgb({skin[0]}, {skin[1]}, {skin[2]});"
    css = ":root{" + cover + "}"
    return css
