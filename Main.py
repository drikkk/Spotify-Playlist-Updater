from app.PlaylistService import PlaylistService

class Main():
    if __name__ == "__main__":
        my_playlists = PlaylistService.get_all_playlists()
        PlaylistService.update_playlists_if_outdated(my_playlists)