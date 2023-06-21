import json
import os

from app.Playlist import Playlist
from app.CustomLogger import CustomLogger
from app.ApiAdapter import ApiAdapter

log = CustomLogger(__name__)


class PlaylistDoctor:
    @staticmethod
    def get_all_playlists():
        PLAYLISTS_FILE = "playlists.json"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        playlists_file_path = os.path.join(current_dir, "..", PLAYLISTS_FILE)

        try:
            with open(playlists_file_path) as playlists_file:
                playlist_data = json.load(playlists_file)
                playlists = [Playlist(**playlist) for playlist in playlist_data]

                for playlist in playlists:
                    playlist_name = playlist.name
                    playlist_id = playlist.id

                    if not playlist_name:
                        log.error(f"{playlist_id}: Playlist name value cannot be empty.")
                        raise ValueError

                    if not playlist_id:
                        log.error(f"{playlist_name}: Playlist Spotify ID value cannot be empty.")
                        raise ValueError

                return playlists
        except FileNotFoundError:
            log.error(f"Could not find {PLAYLISTS_FILE} from the root directory.")
            raise FileNotFoundError()

    @staticmethod
    def examine_and_update_playlist_details(playlists):
        api_adapter = ApiAdapter()

        for playlist in playlists:
            if api_adapter.get_playlist_name(playlist) == playlist.name:
                log.info(f"{playlist.name}: Playlist seems healthy!")
            else:
                log.info(f"{playlist.name}: Playlist is sick, administering medicine!")
                api_adapter.update_name(playlist)
                if playlist.image:
                    api_adapter.update_image(playlist)
                if playlist.description:
                    api_adapter.update_description(playlist)
