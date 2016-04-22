# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
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
#Fetch the table, pull a random row 
#Clean the text for querying, store artist/songName
#Query and store a link for each track
#Serve video in iframe, clickable links for each


#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/patwhatev/Desktop/phantomjs/bin/phantomjs')
driver.get(urls.urlArr[1])
print("heading to:" + urls.urlArr[1])
#BeautifulSoup
url = driver.current_url 
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
soup.find_all("td")

#Business Name
for business in soup.find_all("td"):
	bizname = business.get_text()
	print(bizname)
	
