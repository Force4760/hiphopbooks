from colorthief import ColorThief
import requests


def main_colors(image_url: str) -> tuple:

    # get image from the provided url
    response = requests.get(image_url, stream=True)
    response = response.raw

    # init ColorThief object
    # by converting the response
    color_thief = ColorThief(response)

    # get the dominant color of the image
    dominant_color = color_thief.get_color(quality=1)

    # 3 colors -> 3 list each with 3 values (rgb)
    cover_light = []
    cover_dark = []
    skin_line = []

    # multiply each value in the domiant color
    # by a certain contant for each of the 3 colors
    # 0.5 for light, 0.4 for dark, 0.8 for skin line
    for value in dominant_color:
        cover_light.append(int(value * 0.5))
        cover_dark.append(int(value * 0.4))
        skin_line.append(int(value * 0.8))

    return cover_light, cover_dark, skin_line
