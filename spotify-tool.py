#!/usr/bin/python

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import argparse

parser = argparse.ArgumentParser(description='Like spotify artists and albums based on liked tracks.')
parser.add_argument('--client_id', '-i',  help='spotify client id', required=True)
parser.add_argument('--client_secret', '-s', help='spotify client secret', required=True)
args = parser.parse_args()

scope = 'user-follow-modify user-library-modify user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=args.client_id, client_secret=args.client_secret, redirect_uri='http://example.com', scope=scope))

#looks at all the user's liked songs, and follows the cooresponding artist and saves the coorsponding albums
def update_library():
	results = sp.current_user_saved_tracks(limit=20)
	#actually follow the artists and save the albums of the first 20 results
	follow_artists_and_save_albums_from_tracks(results['items'])
	while results['next']:
		results = sp.next(results)
		#actually follow the artists and save albums in 20 song chunks
		follow_artists_and_save_albums_from_tracks(results['items'])

def follow_artists_and_save_albums_from_tracks(tracks):
	artists = list()
	albums = list()
	i = 0
	for track in tracks:
		artists.append(tracks[i]['track']['album']['artists'][0]['id'])
		albums.append(tracks[i]['track']['album']['id'])
		i = i + 1
	#sp.user_follow_artists(artists)
	sp.current_user_saved_albums_add(albums)
	print(albums)

update_library()