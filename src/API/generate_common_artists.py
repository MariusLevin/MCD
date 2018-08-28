# A simple script to scrape a large number of example artists from spotify.
# This script does not deduplicate the file generated. Use some unix commands to deduplicate:

import spotipy
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials
from string import ascii_lowercase

REQD_ARGS = 3

def main(argc, argv):
  if argc != REQD_ARGS+1:
    print("Usage: {} <filename> <client_key> <secret_key>".format(argv[0]))
  else:
    write_artists(argv[1], argv[2], argv[3])

def write_artists(filename, client, secret):
  client_creds_mgr = SpotifyClientCredentials(client_id=client, client_secret=secret)
  spotify = spotipy.Spotify(client_credentials_manager=client_creds_mgr)

  with open(filename, "w") as the_file:
    for ch in ascii_lowercase:
      for i in range(10):
        results = spotify.search(q='artist:'+ch+'*', type='artist',limit=50,offset=i*50)
        data = results['artists']['items']

        for d in data:
          the_file.write((d['name']+"\n"))

  os.system("awk '!seen[$0]++' {} > {}".format(filename, "deduped_"+filename))
  os.system("mv {} {}".format("deduped_"+filename, filename))

# client: e394642c72f1484fbe9661aecede6d6c
# secret: fbc0bc0391224c1c8360d427c913eb4e

if __name__ == "__main__":
  main(len(sys.argv), sys.argv)
else:
  print(__name__)