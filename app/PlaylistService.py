import json
import os

from app.Playlist import Playlist
from app.LoggingHandler import LoggingHandler
from app.ApiAdapter import ApiAdapter

log = LoggingHandler(__name__)

class PlaylistService:

    @staticmethod
    def get_all_playlists():
        MY_PLAYLISTS_FILE_NAME = "my_playlists.json"

        current_dir = os.path.dirname(os.path.abspath(__file__))
        my_playlists_file = os.path.join(current_dir, "..", MY_PLAYLISTS_FILE_NAME)

        try:
            with open(my_playlists_file) as playlists_file:
                my_playlists_json = json.load(playlists_file)
                playlists_array = [Playlist(**playlist) for playlist in my_playlists_json]

                for playlist in playlists_array:
                    playlist_name = playlist.name
                    playlist_id = playlist.id

                    if not playlist_name:
                        log.error(f"{playlist_id}: Playlist name value cannot be empty...")
                        raise ValueError

                    if not playlist_id:
                        log.error(f"{playlist_name}: Playlist Spotify ID value cannot be empty...")
                        raise ValueError

                return playlists_array
        except FileNotFoundError:
            log.error(f"Could not find {MY_PLAYLISTS_FILE_NAME} from the root directory...")
            raise FileNotFoundError()

    @staticmethod
    def update_playlists_if_outdated(playlists):
        api = ApiAdapter()

        for playlist in playlists:

            if api.get_playlist_name(playlist) != playlist.name:
                
                log.info(f"{playlist.name}: Updating playlist...")
                api.update_name(playlist)
                if playlist.image:
                    api.update_image(playlist)
                if playlist.description:
                    api.update_description(playlist)
