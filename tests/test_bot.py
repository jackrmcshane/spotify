
HOME_DIR = '/home/asimov/'

import sys
sys.path.insert(0, HOME_DIR + 'spotify/')

import unittest
from bots.bot import SpotifyBot
from wrappers.auth import AUTH
from etc import SCOPES, REDIRECT
from credentials import SORTER_CREDS, SAVER_CREDS


class TestBot(unittest.TestCase):

    def setUp(self) -> None:

        self.auth = AUTH(
                SCOPES, SORTER_CREDS['client_id'], SORTER_CREDS['client_secret'], REDIRECT
        )

        self.bot = SpotifyBot(self.auth)


    def tearDown(self) -> None:
        del self.bot

    def test_init(self):
        self.assertIsNotNone(self.bot)





if __name__ == '__main__':

    unittest.main()
