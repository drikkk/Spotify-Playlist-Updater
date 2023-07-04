# Spotify Playlist Doctor

I created this project to fight the Spotify playlist reporting bots.
Creators use bots to spam reports on growing playlists which triggers the Spotify Takedown Notification and your
playlist will be nulled from its title, description and image.

When executed, all playlists in the json file will be checked upon. If a name change is detected for the given playlist, then its name, description and image is updated.
Description and image update can be skipped by setting them as empty ```""``` value in the json file.

When Main.py is run, then playlist checkup, update and error messages are logged to ```output.log``` in project root directory.

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/) (or greater)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Spotify Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)
- [Spotify API Refresher Token](https://developer.spotify.com/documentation/ios/concepts/token-swap-and-refresh)

## Set up and run project

1. Navigate to project root directory
2. Edit ```config.ini``` and fill in your Spotify API Credentials from [Prerequisites](#prerequisites)
3. [Define your playlists](#define-your-playlists)
4. Run command ```pip install -r requirements.txt```
5. Run command ```python3.8 Main.py```

If you have followed these steps without errors then your playlist should have been updated and result logged to ```output.log```

## Define your playlists

1. Get your Public playlist ID: ```https://open.spotify.com/playlist/```__YOUR_PLAYLIST_ID__```?si=83ebb0218ab843cd```
2. Move all your playlist images to: ```/resources/images```
3. Open playlists json file: ```playlists.json```
4. Add your playlists that you wish to keep healthy. 

### Example:

```json
[
    {
        "name": "Example playlist #1",
        "description": "Example description",
        "image": "example_image.jpg",
        "spotifyPlaylistId": "4EAgTGzJpLvtDxQhqNgd0z"
    },
    {
        "name": "Example playlist #2, without description and image",
        "description": "",
        "image": "",
        "spotifyPlaylistId": "6IOBfN7LWZJ8IGfX7i07R1"
    }
]
```

## To Do

1. Move from "refresher_token" to "code": https://github.com/drikkk/Spotify-Playlist-Doctor/issues/2
