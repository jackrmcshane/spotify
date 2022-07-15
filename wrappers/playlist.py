

class Playlist(object):
    """An object wrapper for playlists returned by the Spotipy API"""

    def __init__(self, playlist):
        super(Playlist, self).__init__()
        self.playlist = playlist

    def get_id(self): return self.playlist['id']
    def get_uri(self): return self.playlist['uri']
    def get_name(self): return self.playlist['name']
    def get_descr(self): return self.playlist['description']

    def get_tracks(self, spotify):
        raise Error('This function is not yet implemented.')
