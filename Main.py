from app.PlaylistDoctor import PlaylistDoctor


class Main():
    if __name__ == "__main__":
        my_playlists = PlaylistDoctor.get_all_playlists()
        PlaylistDoctor.examine_and_update_playlist_details(my_playlists)