import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("data.json") as jsonFile:
    authdata = json.load(jsonFile)
    jsonFile.close()

sp_client_id = authdata['sp_client_id']
sp_client_secret = authdata['sp_client_secret']
uri = authdata['uri']


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=sp_client_id,client_secret=sp_client_secret,redirect_uri=uri,scope=scope))

num = 0
dict1 = {}
for i in range(0,1000,50):
    try:
        results = sp.current_user_saved_tracks(limit=50,offset=i)
        list_track = []
        for idx, item in enumerate(results['items']):
            track = item['track']
            strtrack = track['artists'][0]['name'] + "-" + track['name']
            dict1[num] = strtrack
            # print(num, track['artists'][0]['name'], " – ", track['name'])
            num += 1
    except:
        results = sp.current_user_saved_tracks(limit=50,offset=i)
        list_track = []
        for idx, item in enumerate(results['items']):
            track = item['track']
            strtrack = track['artists'][0]['name'] + "-" + track['name']
            dict1[num] = strtrack
            # print(num, track['artists'][0]['name'], " – ", track['name'])
            num += 1

with open('result2.json', 'w') as fp:
    json.dump(dict1, fp)