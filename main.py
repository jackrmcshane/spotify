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
    bot = SpotifyBot(AUTH(scopes, *SECRETS['sorter']))
    # get Liked Songs library from spotify
    # tracks is a list of Track wrapper objects
    # the data returned by spotify does not provide genre,
    # therefore have to use the artist for each track to get the associated genre
    # ie. have to create function for bot to get genre based on artist
    # eg. def get_genre_by_artist(self, artist)
    tracks = bot.get_liked_library()
    print(type(tracks))
    print(type(tracks[0]))

