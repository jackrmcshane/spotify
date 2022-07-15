
class Artist(object):

    def __init__(self, artist):
        super(Artist, self).__init__()
        self.artist = artist

    def get_name(self): return self.artist['name']
    def get_id(self): return self.artist['id']
    def get_uri(self): return self.artist['uri']
    def get_genres(self): return self.artist['genres']
