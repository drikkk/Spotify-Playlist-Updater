import json
import base64
import os
import requests

from app.Configuration import Configuration
from app.LoggingHandler import LoggingHandler

log = LoggingHandler(__name__)

TOKEN = "https://accounts.spotify.com/api/token"
PLAYLISTS = "https://api.spotify.com/v1/playlists"


class ApiAdapter:
    BEARER_STRING = ""

    def __init__(self):
        self.BEARER_STRING = self.get_refreshed_bearer_token()
        
    @staticmethod
    def get_refreshed_bearer_token():
        url = TOKEN
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "refresh_token",
            "refresh_token": Configuration.refresher_token
        }
        auth = (Configuration.client, Configuration.secret)

        try:
            response = requests.post(url, headers=headers, data=data, auth=auth)
            response.raise_for_status()
            return f"Bearer {response.json()['access_token']}"
        except requests.exceptions.RequestException:
            log.error("Failed to get refreshed bearer token.")
            raise RuntimeError()


    def get_playlist_name(self, playlist):
        url = f"{PLAYLISTS}/{playlist.id}"
        headers = {"Authorization": self.BEARER_STRING}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            return response_json["name"]
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            log.error("Failed to get playlist name.")
            raise RuntimeError()


    def update_name(self, playlist):
        url = f"{PLAYLISTS}/{playlist.id}"
        headers = {"Authorization": self.BEARER_STRING, "Content-Type": "application/json"}
        data = json.dumps({"name": playlist.name})

        try:
            response = requests.put(url, headers=headers, data=data)
            status_code = response.status_code

            if status_code == 200:
                log.info(f"{playlist.name}: Name updated!")
            else:
                name_update_failed_error = "Failed to update playlist name."
                error_message = response.json().get("error", name_update_failed_error)
                log.error(f"{playlist.name}: {error_message}. Status code: {status_code}")
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            log.error(name_update_failed_error)


    def update_description(self, playlist):
        url = f"{PLAYLISTS}/{playlist.id}"
        headers = {"Authorization": self.BEARER_STRING, "Content-Type": "application/json"}
        data = json.dumps({"description": playlist.description})

        try:
            response = requests.put(url, headers=headers, data=data)
            status_code = response.status_code

            if status_code == 200:
                log.info(f"{playlist.name}: Description updated!")
            else:
                description_update_failed_error = "Failed to update playlist description."
                error_message = response.json().get("error", description_update_failed_error)
                log.error(f"{playlist.name}: {error_message}. Status code: {status_code}")
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            log.error(description_update_failed_error)


    def update_image(self, playlist):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_file_path = os.path.join(current_dir, "..", "resources", "images", playlist.image)

        with open(image_file_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        url = f"{PLAYLISTS}/{playlist.id}/images"
        headers = {"Authorization": self.BEARER_STRING, "Content-Type": "image/jpeg"}
        data = base64_image

        try:
            response = requests.put(url, headers=headers, data=data)
            status_code = response.status_code

            if status_code == 202:
                log.info(f"{playlist.name}: Image updated!")
            else:
                image_update_failed_error = "Failed to update playlist image."
                error_message = response.json().get("error", image_update_failed_error)
                log.error(f"{playlist.name}: {error_message}. Status code: {status_code}")
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            log.error(image_update_failed_error)
