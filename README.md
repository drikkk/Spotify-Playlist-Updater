# Spotify Playlist Doctor

I created this project to fight the Spotify playlist reporting bots.
Salty creators use bots to spam reports on growing playlists which triggers the Spotify Takedown Notification and your
playlist will be nulled from its title, description and image.

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/) (or greater)

## Set up Python project

- Clone the repository
- Add your Spotify API credentials to config.ini
- Run ```pip install -r requirements.txt```

## Define your playlists

- Get your playlist ID: ```https://open.spotify.com/playlist/YOUR_PLAYLIST_ID?si=83ebb0218ab843cd```
- Move all your playlist images to: ```path/Spotify-Playlist-Doctor/resources/images```
- Edit playlists json file: ```path/Spotify-Playlist-Doctor/playlists.json```
- Configure your playlist name, description, image name and Spotify ID:
```
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
Argument: path\Spotify-Playlist-Doctor\resources\scripts\run.vbs
Start in: path\Spotify-Playlist-Doctor
```

If you have followed all the steps without errors then your playlists will now be checked in the background every 5
minutes and will be updated once playlist name change is detected!
