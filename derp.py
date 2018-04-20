import now_playing
from time import sleep

count = 0

while True:
    network = now_playing.lastfm.connect(now_playing.keys.API_KEY, now_playing.keys.SECRET_KEY)
    track = now_playing.lastfm.current_track(network, "PseudoDesign")
    now_playing.lastfm.save_track_info(track, r'C:\Users\Adam\Documents\Twobbler')
    if count % 6 == 0:
        count = 0
        print("setting track info to {0}".format(track))
    count += 1
    sleep(5)

