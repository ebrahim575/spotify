import spotify as spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import spotipy
import spotipy.util as util
import configparser

import spotipy
import spotipy.oauth2 as oauth2

# drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e7398f843f1a48bab3d2c197aa795d2c",
#                                                client_secret="c218209ac72943a09f9c5d3f4c3193d4",
#                                                redirect_uri="https://www.google.com/",
#                                                scope="user-library-read",
#                                                cache_path='None'))
username = 'spotify:user:ebrahim575'
playlist_id = 'spotify:playlist:6iFHmlL4TUyRvhPo33MHc1'
#
# track_ids = sp.artist_top_tracks(drake_uri)
track_uri = ['5ZSIExfQuVv69tw5Qw3yDl']
#
# for track in track_ids['tracks'][:10]:
#     print('track    : ' + track['id'])


# if len(sys.argv) > 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
# else:
#     print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
#     sys.exit()





config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')


auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)


scope = 'playlist-modify-public'
user = 'ebrahim575'



username = 'ebrahim575'
token = util.prompt_for_user_token(
    username=username,
    scope='playlist-modify-public',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="https://www.google.com/"
)
sp = spotipy.Spotify(auth=token)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(user, playlist_id, track_uri)
    print(results)
else:
    print("Can't get token for", username)