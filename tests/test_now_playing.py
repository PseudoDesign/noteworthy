from unittest import TestCase
from unittest.mock import patch
from now_playing import keys
from now_playing import connection


class TestConnection(TestCase):
    @patch('pylast.LastFMNetwork')
    def test_connect_uses_pylast_and_last_fm(self, last_fm_network):
        api = "api_key"
        secret = "secret_key"
        last_fm_network.return_value = "network"
        return_value = connection.connect(api, secret)
        last_fm_network.assert_called_once_with(api_key=api, api_secret=secret)
        self.assertEqual(return_value, "network");



class TestKeys(TestCase):
    def test_api_key_is_string(self):
        self.assertEqual(type(keys.API_KEY), str)

    def test_secret_key_is_string(self):
        self.assertEqual(type(keys.SECRET_KEY), str)
