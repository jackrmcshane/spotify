import spotipy
from spotipy.oauth2 import SpotifyOAuth


class AUTH(object):
    def __init__(self, scopes, cid, secret, redirect):
        super(AUTH, self).__init__()
        self.cid = cid
        self.secret = secret
        self.redirect = redirect
        self.scopes = scopes
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = cid,
            client_secret=secret,
            redirect_uri=redirect,
            scope=scopes
        ))
