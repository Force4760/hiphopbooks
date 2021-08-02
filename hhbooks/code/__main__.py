from .get_data import album_info, get_album_lyrics
from .treat_data import songs
from .final_render import render
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    G_TOKEN = os.getenv("G_TOKEN")
    SP_CLIENT_ID = os.getenv('SP_CLIENT_ID')
    SP_CLIENT_SECRET = os.getenv('SP_CLIENT_SECRET')
    SP_TOKEN_ID = os.getenv('SP_TOKEN_ID')

    link = input("Link: ").strip()
    album = album_info(link, SP_CLIENT_ID, SP_CLIENT_SECRET, SP_TOKEN_ID)
    tracks = get_album_lyrics(G_TOKEN, album["name"], album["artists"])
    songs_list = songs(album, tracks)
    render(link, songs_list, album)
