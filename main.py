
#!/usr/bin/env python3
import os
import spotipy
import sys

from bots.bot import SpotifyBot
from bots.sorterbot import SorterBot

from credentials import SORTER_CREDS

from wrappers.auth import AUTH
from wrappers.track import Track
from wrappers.playlist import Playlist




def test_spotbot(auth):
    bot = SpotifyBot(auth)
    playlist = bot.get_user_playlists()[0]
    tracks = bot.get_playlist_tracks(playlist.get_uri())
    print(type(tracks), len(tracks))
    for i in range(5):
        print(tracks[i].get_name())



def test_sorter(auth):
    sorter = SorterBot(auth)
    sorter.sort_liked_library()


def test_track_wrapper(auth):
    sorter = SorterBot(auth)
    track = sorter.get_liked_library()[0]
    artists = track.get_artists(sorter.auth)

    genres = track.get_genres(auth)
    print(len(genres))
    for genre in genres:
        print(genre)





def test_artist_wrapper(auth):
    artist = SorterBot(auth).get_liked_library()[0].get_artists(auth)[0]
    genres = artist.get_genres()
    print(type(genres), len(genres))
    for genre in genres:
        print(genre)




if __name__ == '__main__':

    redirect = 'http://localhost:8080/callback'

    scopes = [ # scopes necessary for the bot to do its thing
        'user-library-read',
        'user-library-modify',
        'playlist-modify-public',
        'playlist-modify-private',
        'playlist-read-private'
    ]

    auth = AUTH(
            scopes, 
            SORTER_CREDS['client_id'], 
            SORTER_CREDS['client_secret'],
            redirect
    )


    test_track_wrapper(auth)
