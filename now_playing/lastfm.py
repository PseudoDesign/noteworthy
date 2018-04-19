import pylast


def connect(api_key, secret_key):
    return pylast.LastFMNetwork(api_key=api_key, api_secret=secret_key)

