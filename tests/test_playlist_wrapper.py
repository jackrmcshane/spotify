HOME_DIR = '/home/asimov/'

import sys
sys.path.insert(0, HOME_DIR + 'spotify/')

import unittest
from wrappers.playlist import Playlist
from wrappers.auth import AUTH
from etc import SCOPES, REDIRECT
from credentials import SORTER_CREDS, SAVER_CREDS



class TestPlaylistWrapper(unittest.TestCase):

    """Docstring for TestPlaylistWrapper. """

    def setUp(self) -> None:
        self.auth = AUTH(
                SCOPES, SORTER_CREDS['client_id'], SORTER_CREDS['client_secret'], REDIRECT
        )

        results = self.auth.spotify.current_user_playlists()
        self.playlist = Playlist(results['items'][0])


        
    def tearDown(self) -> None:
        del self.auth
        del self.playlist


    def test_init(self):
        self.assertIsNotNone(self.playlist)

    def test_get_id(self):
        id = self.playlist.playlist['id']
        self.assertIsNotNone(id)
        self.assertEqual(id, self.playlist.get_id())


    def test_get_uri(self):
        uri = self.playlist.playlist['uri']
        self.assertIsNotNone(uri)
        self.assertEqual(uri, self.playlist.get_uri())

    def test_get_name(self):
        name = self.playlist.playlist['name']
        self.assertIsNotNone(name)
        self.assertEqual(name, self.playlist.get_name())

    def test_get_descr(self):
        descr = self.playlist.playlist['description']
        self.assertIsNotNone(descr)
        self.assertEqual(descr, self.playlist.get_descr())




if __name__ == "__main__":
    unittest.main()
