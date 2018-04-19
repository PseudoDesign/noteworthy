from unittest import TestCase
from unittest.mock import patch, MagicMock
from now_playing import keys
from now_playing import lastfm


class TestConnection(TestCase):
    @patch('pylast.LastFMNetwork')
    def test_connect_uses_pylast_and_last_fm(self, last_fm_network):
        api = "api_key"
        secret = "secret_key"
        last_fm_network.return_value = "network"
        return_value = lastfm.connect(api, secret)
        last_fm_network.assert_called_once_with(api_key=api, api_secret=secret)
        self.assertEqual(return_value, "network")

    def test_current_track(self):
        network = MagicMock()
        user = MagicMock()
        track = MagicMock()
        network.get_user.return_value = user
        user.get_now_playing.return_value = track
        username = "test"
        return_value = lastfm.current_track(network, username)
        network.get_user.assert_called_once_with(username)
        user.get_now_playing.assert_called_once()
        self.assertEqual(return_value, track)


class TestKeys(TestCase):
    def test_api_key_is_string(self):
        self.assertEqual(type(keys.API_KEY), str)

    def test_secret_key_is_string(self):
        self.assertEqual(type(keys.SECRET_KEY), str)
