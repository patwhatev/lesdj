# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os

#YelpBot Intro
print('▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀')
print('▒█▄▄▄█ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▀▀▄ ▒█░░▒█ ░▒█░░') 
print('░░▒█░░ ▒█▄▄▄ ▒█▄▄█ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░')

print("YelpBot: Hi there, I am YelpBot")
name =  raw_input("YelpBot: What is your name?")
print"Hey", name 

food = raw_input('YelpBot: What are you craving?')
zipcode = raw_input('YelpBot: What is your Zip Code?')
print  "YelpBot: Got it. Please wait..."

#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/lcruz/Desktop/phantomjs')
driver.get('http://www.yelp.com')
driver.find_element_by_id("find_desc").clear()
driver.find_element_by_id("find_desc").send_keys(food)
print("searching places for ...") + food 
driver.find_element_by_id("dropperText_Mast").clear()
driver.find_element_by_id("dropperText_Mast").send_keys(zipcode)
print ("around...") + zipcode
driver.find_element_by_id("header-search-submit").click()
#BeautifulSoup
url = driver.current_url 
r = requests.get(url)
soup = BeautifulSoup(r.content)
soup.find_all("a",{"class","biz-name"})
print "YelpBot: Here are some nearby places to eat " + food 
print("==========================================================")
for link in soup.find_all("a",{"class","biz-name"}):
	print(link.get_text())
print "YelpBot: Oh yeah! Here are the addresses:" 
soup.find_all("address")
for link in soup.find_all("address"):
	print(link.get_text())

print('YelpBot: Have a good time!') + name 