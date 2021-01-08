import spotipy.util as util
import configparser
import spotipy
import json

def writeToJSONFile(data):
    filePathNameWExt = 'output.json'
    data = json.dumps(data, indent=4)
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
    print(data)
    print('json success')

def add_to_playlist(token,username):
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        #results = sp.user_playlist_add_tracks(user, playlist_id, track_uris)
        #print(results)

        print('add_to_playlist Success')
    else:
        print("Can't get token for", username)
def tests(token,username):
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        #print(sp.me())

        data = sp.current_user_top_artists(limit=10, offset=0, time_range='medium_term')

        json.dumps(data, indent=4)
        print('me success')
    else:
        print("Can't get token for", username)

def main():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
    username = 'spotify:user:ebrahim575'
    user = 'ebrahim575'
    username = 'ebrahim575'
    playlist_id = 'spotify:playlist:6iFHmlL4TUyRvhPo33MHc1'

    token = util.prompt_for_user_token(
        username=username,
        #scope='playlist-modify-public',
        scope = 'user-top-read',
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="https://www.google.com/"
    )
    sp = spotipy.Spotify(auth=token)

    drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'

    track_ids = sp.artist_top_tracks(drake_uri)
    # track_uri = ['5ZSIExfQuVv69tw5Qw3yDl']
    track_uris = []
    for track in track_ids['tracks'][:10]:
        track_uris.append(track['id'])
        # print('track    : ' + track['id'])
    #print(track_uris)

    add_to_playlist(token,username)
    print('main Success')
    tests(token,username)
    data = sp.current_user_top_artists(limit=10, offset=0, time_range='medium_term')

    writeToJSONFile(data)
main()
