#! /usr/bin/python3

import os
from bs4 import BeautifulSoup as bs4
from selenium import webdriver

username = input("Enter username (must be public) : ")
link = "https://www.instagram.com/"+username

browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver")

browser.get(link)

html = browser.page_source
soup = bs4(html,"lxml")
browser.close()


data = soup.findAll("img")
for x in data:
	jpg = x.get("src").split("?")[0].replace("/s640x640/sh0.08","")
	print(jpg)
	os.system("wget -c -N -P ./Images/"+username+" "+jpg)
