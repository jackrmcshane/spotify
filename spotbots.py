"""
File: discover_weekly.py
Author: Jack McShane
Email: jackmcshane@protonmail.com
Github: https://github.com/jackrmcshane/
Description: a python script for saving my discover weekly playlist to a personal playlist
"""


import spotipy
from wrappers import AUTH, Playlist, Track
from spotipy.oauth2 import SpotifyOAuth





class SpotifyBot(object):
    def __init__(self, auth):
        super(SpotifyBot, self).__init__()
        self.auth = auth


    # spotify actually returns a dictionary full of a bunch of metadata
    # only the 'items' field contains what we actually want
    # the items field contains a list of dictionaries
    # each of these dictionaries has two fields:
        # 'added at', 'track'
    # each track is its own dictionary
    def get_liked_library(self):
        results = self.auth.spotify.current_user_saved_tracks()
        tracks = [item['track'] for item in results['items']]
        while results['next']:
            results = self.auth.spotify.next(results)
            tracks.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def get_user_playlists(self):
        results = self.auth.spotify.current_user_playlists()
        playlists = results['items']
        while results['next']:
            results = self.auth.spotify.next(results)
            playlists.extend(results['items'])

        return [Playlist(p, self.auth.spotify) for p in playlists]


    def get_playlist_tracks(self, pid):
        results = self.auth.spotify.playlist_tracks(pid)
        tracks = [item['track'] for item in results['items']]
        while results['next']:
            results = self.auth.spotify.next(results)
            playlists.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def save_tracks_to_playlist(self, pid, tracks):
        self.auth.spotify.user_playlist_add_tracks(self.auth.spotify.current_user(), pid, tracks)






# idea for the sorter bot:
    # rather than sort by artist, sort by genre
class SorterBot(SpotifyBot):
    def __init__(self, auth):
        super(SorterBot, self).__init__(auth)


    def sort_liked_playlist(self):
        # get liked library songs
        # get playlists
        # get tracks for each playlist
        # for each track in liked library,
            # if track.artist is not a playlist
                # create playlist w/ artist name
                # add track to playlist
            # else
                # get corresponding playlist tracks
                # if current track in playlist tracks
                    # next
                # else
                    # add track to playlist
            # remove current track from liked library
        pass



    def get_genres(self):
        # get liked library
        return set(map(lambda track: track.genre, self.get_liked_library()))
        # get genres of each song
        # create a set from the genres
        # return set of genres




class SaverBot(SpotifyBot):


    def __init__(self, auth):
        super(SaverBot, self).__init__(auth)
        self.discover_uri = 'spotify:playlist:37i9dQZEVXcDpi5Jo3ptNB'

    def get_discover_tracks(self):
        return self.get_playlist_tracks(self.discover_uri)

    def save_discover_tracks(self):
        import time

        pname = '{} Discover Weekly'.format(time.strftime('%Y_%m_%d'))
        descr = 'A previous Discover weekly playlist from spotify'
        tracks = list(map(lambda t: t.uri, self.get_discover_tracks()))
        p = Playlist( self.auth.spotify.user_playlist_create(self.auth.spotify.current_user()['id'], pname, public=False, description=descr), self.auth.spotify )

        self.auth.spotify.user_playlist_add_tracks(self.auth.spotify.current_user()['id'], p.uri, tracks)
