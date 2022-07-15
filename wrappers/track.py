from wrappers.artist import Artist

class Track(object):
    """An object wrapper for tracks returned by the Spotipy API"""

    def __init__(self, track):
        super(Track, self).__init__()
        self.track = track

    def get_album(self): return self.track['album']
    def get_duration(self): return self.track['duration_ms']
    def get_explicit(self): return self.track['explicit']
    def get_id(self): return self.track['id']
    def get_name(self): return self.track['name']
    def get_uri(self): return self.track['uri']

    # working!
    def get_artists(self, auth): 
        artists = [auth.spotify.artist(a['id']) for a in self.track['artists']]
        return list(map(Artist, artists))

    # working!!!
    def get_genres(self, auth):
        # gets genres of each artist through their respective get_genres() func.
        genres = list()
        [genres.extend(artist.get_genres()) for artist in self.get_artists(auth)]

        return genres
