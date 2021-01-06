import spotify as spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth






birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e7398f843f1a48bab3d2c197aa795d2c",
                                               client_secret="c218209ac72943a09f9c5d3f4c3193d4",
                                               redirect_uri="https://www.google.com/",
                                               scope="user-library-read",
                                               cache_path='None'))
spotify = sp
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])