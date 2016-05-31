# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import os
import re
from core_urls import urlArr
from core_videoParts import videoParts
import core_videoParts
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

#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/patwhatev/Desktop/phantomjs/bin/phantomjs')
#Generate n video parts
query = raw_input('WELCOME TO LES DJ \n\nHOW MANY TRACKS IN YOUR PLAYLIST?\n') 
print("\nGathering . . . \n")
playlist = []

for i in range(0, int(query)):
	video = random.choice(videoParts)
	title = video[0]
	part = random.choice(video[1])
	skater = part[0]
	artist = part[1]
	song = part[2]
	if artist == song: 
		artist = skater
		skater = "No Part/Skater Listed"


	trackPrint = (artist + " - " + song)
	storeTrack = (artist + " " + song)
	print("\nTITLE: " + title)
	print("PART: " + skater)
	print("TRACK: " + trackPrint)
	partArr = [title,skater,storeTrack]
	playlist.append(partArr)

print(playlist)
	# for row in tracklist.find_all("td"):
	# 	pageText = row.get_text().encode('utf-8')
	# 	arr = ["?"]
	# 	if "-" in pageText and any(x not in pageText for x in arr):
	# 		splitStr = pageText.split("-")
	# 		if len(splitStr) < 2:
	# 			continue

	# 		part = splitStr[0].strip()
	# 		artist = splitStr[1].strip()
	# 		song = splitStr[-1].strip()
	# 		# print('PART:')
	# 		# print(part)
	# 		# print('ARTIST:')
	# 		# print(artist)
	# 		# print('SONG:')
	# 		# print(song)
	# 		partArr = [part,artist,song] 
	# 		soundtrack.append(partArr)

	# if len(soundtrack) > 1:
	# 	print("Found: " + str(len(soundtrack)) + " Tracks. Writing: " + title + " To File")
	# 	video_arr = [title, soundtrack]
	# 	with open("videoparts.py", "a") as parts:	
	# 		parts.write(str(video_arr))
	# else: 
	# 	continue

		# randomTrack = random.choice(soundtrack)
		# print('APPENDING:')
		# print(randomTrack)
		# playlist.append(randomTrack)

	# print(playlist)





