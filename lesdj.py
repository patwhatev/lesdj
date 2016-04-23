# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import os
import re
import urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Sk9Bot Intro
print('$$\       $$$$$$$$\  $$$$$$\  $$$$$$$\     $$$$$\ ')
print('$$ |      $$  _____|$$  __$$\ $$  __$$\    \__$$ |')
print('$$ |      $$ |      $$ /  \__|$$ |  $$ |      $$ |')
print('$$ |      $$$$$\    \$$$$$$\  $$ |  $$ |      $$ |')
print('$$ |      $$  __|    \____$$\ $$ |  $$ |$$\   $$ |')
print('$$ |      $$ |      $$\   $$ |$$ |  $$ |$$ |  $$ |')
print('$$$$$$$$\ $$$$$$$$\ \$$$$$$  |$$$$$$$  |\$$$$$$  |')
print('\________|\________| \______/ \_______/  \______/ ')

query = raw_input('WELCOME TO LES DJ \n\nNAME A VIDEO \n')
print("ITE MAN I GOT U")
#Create a playlist of songs from skate videos 

#First, call a url from URLs
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
print(rand_urls)
for i in range(0, 24):
	driver.get(rand_urls[i])
	print("heading to:" + rand_urls[i])
	url = driver.current_url 
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")

	for webpage in soup.find_all("td"):
		pageText = webpage.get_text()
		arr = ["1","2","3","4","5"]
		if "-" in pageText and any(x not in pageText for x in arr):
			print(pageText)

#BeautifulSoup

