from . import lastfm
from . import keys
from time import sleep
import argparse


def run(username, working_directory):
    while True:
        network = lastfm.connect(keys.API_KEY, keys.SECRET_KEY)
        track = lastfm.current_track(network, username)
        lastfm.save_track_info(track, working_directory)
        sleep(5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("working_directory")
    args = parser.parse_args()

    run(args.username, args.working_directory)

