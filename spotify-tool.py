#!/usr/bin/python

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse

parser = argparse.ArgumentParser(description='Like spotify artists and albums based on liked tracks.')
parser.add_argument('--client_id', '-i',  help='spotify client id', required=True)
parser.add_argument('--client_secret', '-s', help='spotify client secret', required=True)
args = parser.parse_args()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=args.client_id, client_secret=args.client_secret))

#TODO the program lol

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
