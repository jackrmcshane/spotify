
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from bots.bot import SpotifyBot

from wrappers.auth import AUTH
from wrappers.playlist import Playlist
from wrappers.track import Track



class SorterBot(SpotifyBot):

    def __init__(self, auth):
        super(SorterBot, self).__init__(auth)


    # working!
    def get_liked_library(self):
        results = self.auth.spotify.current_user_saved_tracks()
        tracks = [item['track'] for item in results['items']]

        while results['next']:
            results = self.auth.spotify.next(results)
            tracks.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def sort_liked_library(self):
        # get liked library songs
        liked_tracks = self.get_liked_library()
        # get playlists
        user_playlists = self.get_user_playlists()
        # get tracks for each playlist
        tracks = [self.get_playlist_tracks(p.get_id()) for p in user_playlists]
        # zip playlists together with their tracks
        pairs = list(zip(user_playlists, tracks))

        # for each track in liked library,
        for track in liked_tracks:
            # get track artist
            genre = track.get_genres()
            # get track genre from track artist
            # for each genre of track
                # if genre is already a playlist
                    # check that track is not already in playlist
                    # if track is in playlist
                        # continue
                    # else
                        # add track to playlist
                # else
                    # create playlist
                    # add track to playlist
            # remove track from liked library
        pass
