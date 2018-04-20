import now_playing


network = now_playing.lastfm.connect(now_playing.keys.API_KEY, now_playing.keys.SECRET_KEY)

track = now_playing.lastfm.current_track(network, "PseudoDesign")

now_playing.lastfm.save_track_info(track, r'C:\Users\Adam\Documents\Twobbler')

