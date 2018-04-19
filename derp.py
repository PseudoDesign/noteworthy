import now_playing


network = now_playing.lastfm.connect(now_playing.keys.API_KEY, now_playing.keys.SECRET_KEY)

print("Network: " + str(network))

track = network.get_user("PseudoDesign").get_now_playing()

print(track.artist)
print(track.title)
album = track.get_album()
album_title = album.title
album_image = album.get_cover_image()
print(album)
