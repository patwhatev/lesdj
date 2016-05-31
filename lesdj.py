# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import os
import re
import urls
from urls import urlArr
import videoparts
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print('$$\       $$$$$$$$\  $$$$$$\  $$$$$$$\     $$$$$\ ')
print('$$ |      $$  _____|$$  __$$\ $$  __$$\    \__$$ |')
print('$$ |      $$ |      $$ /  \__|$$ |  $$ |      $$ |')
print('$$ |      $$$$$\    \$$$$$$\  $$ |  $$ |      $$ |')
print('$$ |      $$  __|    \____$$\ $$ |  $$ |$$\   $$ |')
print('$$ |      $$ |      $$\   $$ |$$ |  $$ |$$ |  $$ |')
print('$$$$$$$$\ $$$$$$$$\ \$$$$$$  |$$$$$$$  |\$$$$$$  |')
print('\________|\________| \______/ \_______/  \______/ ')

print("\nRUNNING\n")

#Query and store a link for each track
#Serve video in iframe, clickable links for each

#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/patwhatev/Desktop/phantomjs/bin/phantomjs')
#Generate 25 random URLs 
rand_urls = random.sample(urls.urlArr, 25)
print("\nGathering urls. . . \n")
playlist = []

for i in range(2244, 2355):
	soundtrack = []
	print("heading to: " + urlArr[i])
	driver.get(urlArr[i])
	url = driver.current_url 
	urlString = str(url)
	titleString = str(urlString.split('/')[4])
	title = re.sub('-',' ',titleString)
	print("FOUND TITLE:")
	print(title)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	tracklist = soup.find("table", {"id" : "soundtracklist"})
	for row in tracklist.find_all("td"):
		pageText = row.get_text().encode('utf-8')
		arr = ["?"]
		if "-" in pageText and any(x not in pageText for x in arr):
			splitStr = pageText.split("-")
			if len(splitStr) < 2:
				continue

			part = splitStr[0].strip()
			artist = splitStr[1].strip()
			song = splitStr[-1].strip()
			# print('PART:')
			# print(part)
			# print('ARTIST:')
			# print(artist)
			# print('SONG:')
			# print(song)
			partArr = [part,artist,song] 
			soundtrack.append(partArr)

	if len(soundtrack) > 1:
		print("Found: " + str(len(soundtrack)) + " Tracks. Writing: " + title + " To File")
		video_arr = [title, soundtrack]
		with open("videoparts.py", "a") as parts:	
			parts.write(str(video_arr))
	else: 
		continue

		# randomTrack = random.choice(soundtrack)
		# print('APPENDING:')
		# print(randomTrack)
		# playlist.append(randomTrack)

	# print(playlist)


		

#BeautifulSoup




