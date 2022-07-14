

from spotipy import SpotifyOAuth
from wrappers.auth import AUTH
from wrappers.track import Track
from wrappers.playlist import Playlist




class SpotifyBot(object):

    def __init__(self, auth):
        super(SpotifyBot, self).__init__()
        self.auth = auth
        print('successful init')


    def get_user_playlists(self):

        results = self.auth.spotify.current_user_playlists()
        playlists = results['items']

        while results['next']: # while there are more pages
            results = self.auth.spotify.next(results)
            playlists.extend(results['items'])

        return [playlist.Playlist(p) for p in playlists]
