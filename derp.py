import noteworthy
from time import sleep

count = 0

while True:
    network = noteworthy.lastfm.connect(noteworthy.keys.API_KEY, noteworthy.keys.SECRET_KEY)
    track = noteworthy.lastfm.current_track(network, "PseudoDesign")
    noteworthy.lastfm.save_track_info(track, r'C:\Users\Adam\Documents\Twobbler')
    if count % 6 == 0:
        count = 0
        print("setting track info to {0}".format(track))
    count += 1
    sleep(5)

