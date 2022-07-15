import spotipy
from spotipy.oauth2 import SpotifyOAuth


class AUTH(object):
    def __init__(self, scope, cid, secret, redirect):
        super(AUTH, self).__init__()
        self.cid = cid
        self.secret = secret
        self.redirect = redirect
        self.scope = scope
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = cid,
            client_secret=secret,
            redirect_uri=redirect,
            scope=scope
        ))




class Playlist(object):
    """An object wrapper for playlists returned by the Spotify REST API"""
    def __init__(self, playlist, spotify):
        super(Playlist, self).__init__()
        self.playlist = playlist
        self.uri = playlist['uri']
        self.id = playlist['id']
        self.name = playlist['name']
        self.snapshot_id = playlist['snapshot_id']
        self.tracks = self._get_tracks(spotify)

        self.collab = playlist['collaborative']
        self.description = playlist['description']
        self.external_urls = playlist['external_urls']
        self.href = playlist['href']
        self.owner = playlist['owner']
        self.public = playlist['public']


    def _get_tracks(self, spotify):
        results = spotify.playlist_tracks(self.id)
        tracks = [item['track'] for item in results['items']]
        while results['next']:
            results = spotify.next(results)
            tracks.extend([item['track'] for item in results['items']])

        self.tracks = list(map(Track, tracks))



# can maybe use as so:
# tracks = list(map(Track, track_list))
class Track(object):
    """Object wrapper for tracks returned by the Spotify REST API"""
    def __init__(self, track):
        super(Track, self).__init__()
        self.track = track
        self.album = track['album']
        self.artists = track['artists']
        self.duration_ms = track['duration_ms']
        self.explicit = track['explicit']
        self.id = track['id']
        self.name = track['name']
        self.uri = track['uri']
