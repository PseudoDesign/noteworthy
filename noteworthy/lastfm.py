import pylast
import os
import wget
import shutil

DEFAULT_TILE = "No Track Info"
DEFAULT_ARTIST = ""
DEFAULT_ALBUM = ""
DEFAULT_LONG_INFO = "No Track Info    "
DEFAULT_IMAGE_NAME = "default.png"


def set_default_image(directory, filename):
    default_file = os.path.join(directory, DEFAULT_IMAGE_NAME)
    new_file = os.path.join(directory, filename)
    shutil.copyfile(default_file, new_file)


def save_text(text, directory, filename):
    file = os.path.join(directory, filename)
    with open(file, 'w') as fpt:
        fpt.write(text)


def save_image(url, directory, filename):
    try:
        file = os.path.join(directory, filename)
        new_file = wget.download(url, out=file)
        os.replace(new_file, file)
    except:
        set_default_image(directory, filename)


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
    if track:
        album = track.get_album()
        save_text(track.title, location, 'title.txt')
        save_text(track.artist.name, location, 'artist.txt')
        save_text(track.title + " - " + track.artist.name + "    ", location, 'long_info.txt')
        if album:
            save_text(album.title, location, 'album.txt')
            save_image(album.get_cover_image(), location, 'album_art.png')
        else:
            save_text(DEFAULT_ALBUM, location, 'album.txt')
            set_default_image(location, 'album_art.png')
    else:
        save_text(DEFAULT_TILE, location, 'title.txt')
        save_text(DEFAULT_ARTIST, location, 'artist.txt')
        save_text(DEFAULT_ALBUM, location, 'album.txt')
        save_text(DEFAULT_LONG_INFO, location, 'long_info.txt')
        set_default_image(location, 'album_art.png')
