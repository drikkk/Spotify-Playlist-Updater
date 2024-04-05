from app.PlaylistUpdaterService import PlaylistUpdaterService

class Main():
    if __name__ == "__main__":
        my_playlists = PlaylistUpdaterService.get_all_playlists()
        PlaylistUpdaterService.update_playlists_if_outdated(my_playlists)