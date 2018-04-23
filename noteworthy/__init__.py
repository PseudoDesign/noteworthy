from . import lastfm
from . import keys
from time import sleep
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    print(args.echo)

    while True:
        network = lastfm.connect(keys.API_KEY, keys.SECRET_KEY)
        track = lastfm.current_track(network, "PseudoDesign")
        lastfm.save_track_info(track, r'C:\Users\Adam\Documents\Twobbler')
        sleep(5)

