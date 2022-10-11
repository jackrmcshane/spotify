
HOME_DIR = '/home/asimov/'

import sys
sys.path.insert(0, HOME_DIR + 'spotify/')

import unittest
from wrappers.playlist import Playlist
from wrappers.track import Track
from wrappers.auth import AUTH
from etc import SCOPES, REDIRECT
from credentials import SORTER_CREDS, SAVER_CREDS



class TestTrackWrapper(unittest.TestCase):

    """Docstring for TestTrackWrapper. """

    def setUp(self) -> None:
        self.auth = AUTH(
                SCOPES, SORTER_CREDS['client_id'], SORTER_CREDS['client_secret'], REDIRECT
        )

        results = self.auth.spotify.current_user_playlists()
        self.playlist = Playlist(results['items'][0])


    def tearDown(self) -> None:
        pass


    

        
