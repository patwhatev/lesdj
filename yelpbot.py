# -*- coding: utf-8 -*-
from __future__ import print_function
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

query = raw_input('WELCOME TO LES DJ \n\nNAME A VIDEO \n')
# zipcode = raw_input('YelpBot: What is your Zip Code?')
print("ITE MAN I GOT U")

#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/peverman/Desktop/phantomjs/bin/phantomjs')
driver.get('http://www.skatevideosite.com/soundtracks')
driver.find_element_by_name("searchterm").clear()
driver.find_element_by_name("searchterm").send_keys(query)
print("Searching For: "+ query)
driver.find_element_by_css_selector('input[name="submit"]').click()
print("started search . . .")
results = driver.find_elements_by_css_selector('.skatevideo a')
for result in results[::3]:
    url = result.get_attribute("href")
    if 'soundtrack' in url: 
    	print("storing " + url)
    	with open("urls.py", "a") as myfile:
    		myfile.write('"'+ url + '",\n')


# #BeautifulSoup
# url = driver.current_url 
# r = requests.get(url)
# soup = BeautifulSoup(r.content)
# soup.find_all("a",{"class","biz-name"})

# #Business Name
# for business in soup.find_all("a",{"class","biz-name"}):
# 	bizname = business.get_text()
# 	print bizname
	
# #Address
# soup.find_all("address","biz-name")
# for address in soup.find_all("address"):
# 	location = address.get_text()
# 	print location



# print('YelpBot: Have a good time!') + name 