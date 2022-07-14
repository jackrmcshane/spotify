
#!/usr/bin/env python3
import os
import spotipy
import sys

from bots.bot import SpotifyBot
from credentials import SORTER_CREDS
from wrappers.auth import AUTH
from wrappers.track import Track
from wrappers.playlist import Playlist



if __name__ == '__main__':

    redirect = 'http://localhost:8080'

    # scopes necessary for the bot to do its thing
    scopes = [
        'user-library-read',
        'user-library-modify',
        'playlist-modify-public',
        'playlist-modify-private',
        'playlist-read-private'
    ]




    playlist = Playlist('first playlist')
    auth = AUTH(
            scopes, 
            SORTER_CREDS['client_id'], 
            SORTER_CREDS['client_secret'], 
            redirect
    )


    bot = SpotifyBot(auth)
    playlists = bot.get_user_playlists()
    print(type(playlists), len(playlists))
    for i in range(5):
        print(playlists[i].get_name())
