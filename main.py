import spotipy.util as util
import configparser
import spotipy
import json

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
    scope = 'user-top-read playlist-modify-public',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="https://www.google.com/"
)
sp = spotipy.Spotify(auth=token)

def curr_user_top_tracks_call():
    data = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
    writeToJSONFile2(data)
    print()
    print(data)
    #for i in range(50):
        #print(data['items'][i]['name'])  # reads the json file in a specific way

def read_json2():
    with open('output2.json') as f:
        data = json.load(f) #set data to the loaded file
    return data
    #print(data) #prints all data

#show user top artists
def curr_user_top_artists_make_call():
    data = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
    writeToJSONFile(data)
    print()  # newline
    for i in range(50):
        print(data['items'][i]['name'])  # reads the json file in a specific way

def curr_user_top_artists_json():
    data = read_json()
    for i in range(50):
        print(data['items'][i]['name'])  # reads the json file in a specific way

def curr_user_top_tracks_json():
    data = read_json2()
    print(data)
    for i in range(50):
        print(data['items'][i]['name'])  # reads the json file in a specific way


#function to print all artist top tracks
def artist_top_tracks():
    drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4' #provide URI
    track_ids = sp.artist_top_tracks(drake_uri) #your provided URI
    track_uris = [] #create empty arr
    for track in track_ids['tracks'][:10]: #can only print 10 for 10 requests limited
        track_uris.append(track['id'])
        #print('track    : ' + track['id'])
    print(track_uris) #can print the uris in array format

def mytop10():
    track_uris = [] #create empty arr
    data = read_json2()
    for i in range(50):
        #print(data['items'][i]['id'])  # reads the json file in a specific way
        track_uris.append(data['items'][i]['id'])  # reads the json file in a specific way
    print(track_uris)
    return track_uris

#function to just read json, can use this to read from top
def read_json():
    with open('output.json') as f:
        data = json.load(f) #set data to the loaded file
    return data
    #print(data) #prints all data

#This is writing to a json file
def writeToJSONFile(data):
    filePathNameWExt = 'output.json'
    data = json.dumps(data, indent = 4) #prettys the json file
    with open(filePathNameWExt, 'w') as fp: #this writes to the json file
        fp.write(data) #write with correct format

def writeToJSONFile2(data):
    filePathNameWExt = 'output2.json'
    data = json.dumps(data, indent = 4) #prettys the json file
    with open(filePathNameWExt, 'w') as fp: #this writes to the json file
        fp.write(data) #write with correct format

#function to add songs to playlist
def add_to_playlist():
    track_uris = mytop10()
    if token:
        sp.trace = False
        results = sp.user_playlist_add_tracks(user, playlist_id, track_uris)
        #print(results)
    else:
        print("Can't get token for", username)


def main():
    #curr_user_top_artists_make_call()
    #curr_user_top_tracks_json()
    add_to_playlist()
main()
