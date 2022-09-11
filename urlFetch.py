# from future import print_function
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import datetime
import random
import os
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("\nRUNNING\n")

#PhantomJS
options = Options()
options.add_argument('-headless')
driver = Firefox()
wait = WebDriverWait(driver, timeout=10)

# Auth to spotify
scope = "playlist-modify-public"
sp_auth_id = os.environ['SPOTIPY_CLIENT_ID']
sp_auth_pw = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = 'https://example.com/callback'

sp_auth=spotipy.oauth2.SpotifyOAuth(sp_auth_id, sp_auth_pw, redirect_uri, scope="playlist-modify-public user-library-read")
auth_token = sp_auth.get_access_token()

print(auth_token)
sp = spotipy.Spotify(auth=auth_token['access_token'])

# gather input from user on what bands they are into this week
pref_string = input("What are you into this week? - ")

# separate on commas
pref_array = pref_string.split(",")

# generate new playlist with mm/dd/yyyy as the title
# Create Playlist
current_day = datetime.date.today()
formatted_date = datetime.date.strftime(current_day, "%m/%d/%Y")
title = "shit that sounds like " + pref_string

try:
	# use your own username (found in https://www.spotify.com/us/account/overview)
	user_id = os.environ['SPOTIFY_USERNAME']

	playlist = sp.user_playlist_create(user_id, name=title, public=True, description='╭∩╮（︶︿︶）╭∩╮ Created by @patwhatev')

	print('Created playlist: ' + title)
	playlist_id = playlist['id']

	# iterate through list, search for each band/album
	for pick in pref_array:

		# take pick, search the music map api
		split_pick = pick.split(" ")
		formatted_pick = "+".join(split_pick)

		url = 'https://www.music-map.com/' + pick

		artists = []
		print("heading to: " + url)
		driver.get(url)
		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html.parser")
		found = soup.select_one("#the_title")
		artist_arr = []
		if found:
			artists = soup.select("#gnodMap a")

			# clean up the selected results from the page
			for artist in artists:
				artist_text = artist.get_text()

				# don't include the artist the person already likes
				if not pick.lower() == artist_text.lower():
					artist_arr.append(artist_text)


			# go through all the similar artists from prev array, push track to list and append to playlist
			for artist in artist_arr:
				track_arr = []
				lowered_artist = artist.lower()

				print("artist: ", artist)
				query = "artist:" + artist
				results = sp.search(q=query, limit=20)

				tracks = results['tracks']['items']
				if tracks:
					for track in tracks:
						found_artist = track['artists'][0]['name']
						lowered_found_artist = found_artist.lower()

						if lowered_found_artist == lowered_artist:
							track_id = track['uri']
							tid_arr = track_id.split(':')
							last_elem = tid_arr[-1]

							# Add song ids to temporary array
							track_arr.append(last_elem)

						else: 
							print("filtered out result due to mismatch. lowered_found_artist: " + lowered_found_artist + " lowered_artist: " + lowered_artist)
				else:
					# Add failed lookups to failure array
					print('Unable to find results for: ', artist)

				if len(track_arr) > 0:
					sp.user_playlist_add_tracks(user_id, playlist_id, track_arr)
		else:
			print('unable to find: ' + pick)
except Exception as e:
	print(e)
