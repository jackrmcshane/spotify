"""
File: discover_weekly.py
Author: Jack McShane
Email: jackmcshane@protonmail.com
Github: https://github.com/jackrmcshane/
Description: a python script for saving my discover weekly playlist to a personal playlist
"""


import spotipy
from wrappers import AUTH, Playlist, Track, Artist
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
        # first page of results
        results = self.auth.spotify.playlist_tracks(pid)
        # extract tracks from first page of results
        tracks = [item['track'] for item in results['items']]
        # while there is another page
        while results['next']:
            # reassign results var
            results = self.auth.spotify.next(results)
            tracks.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def save_tracks_to_playlist(self, pid, tracks):
        self.auth.spotify.user_playlist_add_tracks(self.auth.spotify.current_user(), pid, tracks)


    # takes one Track object and returns a list of corresponding Artist objects
    def get_artists_by_track(self, track: Track):
        # return artists for the track
        # extract a list of uris from track.track
        uris = list(map(lambda artist: artist['uri'], track.track['artists']))
        # list(map(Artist, track.track['artists']))
        # artists = self.auth.spotify.artists(track.uri)['artists']
        return list(map(Artist, self.auth.spotify.artists(uris)['artists']))





# idea for the sorter bot:
    # rather than sort by artist, sort by genre
class SorterBot(SpotifyBot):
    def __init__(self, auth):
        super(SorterBot, self).__init__(auth)


    def sort_liked_library(self):
        # get liked library songs
        liked_tracks = self.get_liked_library()

        for track in liked_tracks:
            track.artists = self.get_artists_by_track(track)

        # get each playlist under 'Genres' folder
        playlists = self.get_user_playlists()
        [print(p.name) for p in playlists]

        # for each track in liked_tracks
        for track in liked_tracks:
            track_genres = list()
            [track_genres.extend(artist.genres) for artist in track.artists]
            # for each genre in track.genres
            for genre in track_genres:
                # if playlist does not exist
                if genre not in list(map(lambda p: p.name, playlists)):
                    # create playlist
                    # add song to playlist
                    pass
                else:
                    # if track not in playlist
                        # add track to playlist
                    pass
            # delete track from liked library



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
