# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
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

# print("YelpBot: Hi there, I am YelpBot")
# name =  raw_input("YelpBot: What is your name?")
# print"YelpBot: Hey", name 

query = raw_input('YelpBot: What are you craving?')
# zipcode = raw_input('YelpBot: What is your Zip Code?')
print  "YelpBot: Got it. Please wait..."

#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/peverman/Desktop/phantomjs/bin/phantomjs')
driver.get('http://www.skatevideosite.com/soundtracks')
driver.find_element_by_name("searchterm").clear()
driver.find_element_by_name("searchterm").send_keys(query)
driver.find_element_by_name("submit").click()
print("searching matches for ...") + query 
driver.find_element_by_css_selector(".skatevideo .blacktitle").click()
print("made it this far")
output = driver.find_element_by_id("soundtracklist")
print output
driver.find_element_by_id("header-search-submit").click()
#BeautifulSoup
url = driver.current_url 
r = requests.get(url)
soup = BeautifulSoup(r.content)
soup.find_all("a",{"class","biz-name"})
print "YelpBot: Here are some nearby places to eat " + food 
print("==========================================================")

#Business Name
for business in soup.find_all("a",{"class","biz-name"}):
	bizname = business.get_text()
	print bizname
	
#Address
soup.find_all("address","biz-name")
for address in soup.find_all("address"):
	location = address.get_text()
	print location



# print('YelpBot: Have a good time!') + name 