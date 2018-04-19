import pylast


def connect(api_key, secret_key):
    """
    Creates a network connection used throughout this module
    :param api_key:
    :param secret_key:
    :return: a pylast network object
    """
    return pylast.LastFMNetwork(api_key=api_key, api_secret=secret_key)


def current_track(network, username):
    """
    Get the current track info for a user
    :param network: a pylast network object
    :param username: The name of the user to inspect
    :return:
    """
    return network.get_user(username).get_now_playing()
