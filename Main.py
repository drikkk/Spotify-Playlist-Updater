from app.PlaylistDoctor import PlaylistDoctor


class Main():
    if __name__ == "__main__":
        my_playlists = PlaylistDoctor.get_all_patients()
        PlaylistDoctor.diagnose_and_cure_patients(my_playlists)