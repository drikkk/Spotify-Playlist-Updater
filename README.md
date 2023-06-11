# Spotify Playlist Doctor

I created this project to fight the Spotify playlist reporting bots.
Creators use bots to spam reports on growing playlists which triggers the Spotify Takedown Notification and your
playlist will be nulled from its title, description and image.

When executed, all playlists in the json file will be checked upon. If a name change is detected for the given playlist, then its name, description and image is updated.
Description and image update can be skipped by setting them as empty ```""``` value in the json file.

Results of the run are logged to output.log in project root.

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/) (or greater)
- [Spotify Client ID and Client Secret](https://developer.spotify.com/documentation/web-api/concepts/apps)
- [Spotify API Refresher Token](https://developer.spotify.com/documentation/ios/concepts/token-swap-and-refresh)

## Set up Python project

- Navigate to project root directory
- Execute ```pip install -r requirements.txt```
- Edit ```config.ini``` and fill in your Spotify API Credentials from [Prerequisites](#prerequisites)

## Define your playlists

- Get your playlist ID from your Spotify playlist URL: ```https://open.spotify.com/playlist/YOUR_PLAYLIST_ID?si=83ebb0218ab843cd```
- Move all your playlist images to: ```C:/Spotify-Playlist-Doctor/resources/images```
- Edit playlists json file: ```C:/Spotify-Playlist-Doctor/playlists.json```
- Add your playlist name, description, image name and Spotify ID:
```json
{
    "name": "Example playlist",
    "description": "Example description",
    "image": "example_image.jpg",
    "spotifyPlaylistId": "EXAMPLE_ID"
},
{
    "name": "Playlist without description and image",
    "description": "",
    "image": "",
    "spotifyPlaylistId": "6IOBfN7LWZJ8IGfX7i07R1"
}
```

## Running every 5 minutes in the background on your Windows machine

Open Task Scheduler and create a new task to run a program with admin permissions, schedule it to 5 minutes interval
after first run.
```
Program to start: C:\Windows\System32\wscript.exe
Argument: C:\Spotify-Playlist-Doctor\resources\scripts\run.vbs
Start in: C:\Spotify-Playlist-Doctor\resources\scripts\
```
If you have followed all the steps without errors then your playlists will now be checked in the background every 5
minutes and will be updated once playlist name change is detected!
