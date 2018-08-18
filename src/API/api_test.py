import spotipy
from sys import argv

from spotipy.oauth2 import SpotifyClientCredentials

client_creds_mgr = SpotifyClientCredentials(client_id=argv[1], client_secret=argv[2])

spotify = spotipy.Spotify(client_credentials_manager=client_creds_mgr)
results = spotify.search(q='artist:weezer', type='artist')

data = results['artists']['items']

for d in data:
  print(d['name'])

# client: e394642c72f1484fbe9661aecede6d6c
# secret: fbc0bc0391224c1c8360d427c913eb4e
