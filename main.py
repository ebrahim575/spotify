import spotify as spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth






lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e7398f843f1a48bab3d2c197aa795d2c",
                                               client_secret="c218209ac72943a09f9c5d3f4c3193d4",
                                               redirect_uri="https://www.google.com/",
                                               scope="user-library-read",
                                               cache_path='None'))
spotify = sp
results = spotify.artist_top_tracks(drake_uri)

for track in results['tracks'][:100]:
    print('track    : ' + track['name'])

    print()