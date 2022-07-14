#!/usr/bin/env python3

import os
import sys
import spotipy
from spotbots import SpotifyBot, SaverBot, SorterBot
from wrappers import AUTH, Playlist, Track
from spotipy.oauth2 import SpotifyOAuth
from secrets import SECRETS


if __name__ == "__main__":


    # scopes necessary for the bot to do its thing
    scopes = [
        'user-library-read',
        'user-library-modify',
        'playlist-modify-public',
        'playlist-modify-private',
        'playlist-read-private'
    ]


    # initialize bot
    bot = SpotifyBot(AUTH(scopes, *SECRETS['discover']))
    # get Liked Songs library from spotify
    tracks = bot.get_liked_library()
    print(len(tracks))
