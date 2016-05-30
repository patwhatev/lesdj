# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import os
import re
import urls
import videoParts
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

# query = raw_input(' \n\n\nENTER TEXT HERE: ')
print("\nRUNNING\n")

#Log the video title 
#(Take the URL and use regex to clean it up)
#Fetch the table, pull a random row 
#Clean the text for querying, store artist/songName
#Query and store a link for each track
#Serve video in iframe, clickable links for each

#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/patwhatev/Desktop/phantomjs/bin/phantomjs')
#Generate 25 random URLs 
rand_urls = random.sample(urls.urlArr, 25)
print("\nGathering urls. . . \n")
playlist = []

for i in range(0, 24):
	soundtrack = []
	print("heading to: " + rand_urls[i])
	driver.get(rand_urls[i])
	url = driver.current_url 
	urlString = str(url)
	titleString = str(urlString.split('/')[4])
	final = re.sub('-',' ',titleString)
	print("TITLE:")
	print(final)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	for webpage in soup.find_all("tr", {"class" : "list"}):
		pageText = webpage.get_text().encode('utf-8')
		arr = ["1","2","3","4","5"]
		if "-" in pageText and any(x not in pageText for x in arr):
			splitStr = pageText.split("-")
			if len(splitStr) <= 2:
				continue

			part = splitStr[0]
			artist = splitStr[1]
			song = splitStr[-1]
			print('PART:')
			print(part)
			print('ARTIST:')
			print(artist)
			print('SONG:')
			print(song)
			partArr = [final,part,artist,song] 
			soundtrack.append(partArr)

	if len(soundtrack) > 1:
		randomTrack = random.choice(soundtrack)
		print('APPENDING:')
		print(randomTrack)
		playlist.append(randomTrack)

	print(playlist)


		

#BeautifulSoup




