import pylast
import os
import wget


def save_text(text, directory, filename):
    file = os.path.join(directory, filename)
    with open(file, 'w') as fpt:
        fpt.write(text)


def save_image(url, directory, filename):
    file = os.path.join(directory, filename)
    wget.download(url, out=file)


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


def save_track_info(track, location):
    """
    Save the track info (artist, title, album, cover) to location
    :param track:
    :param location: File path to save to
    :return:
    """
    album = track.get_album()
    save_text(track.title, location, 'title.txt')
    save_text(track.artist.name, location, 'artist.txt')
    save_text(album.title, location, 'album.txt')
    save_image(album.get_cover_image(), location, 'album_art.png')
