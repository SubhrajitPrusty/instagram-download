#! /usr/bin/python3

import os
from bs4 import BeautifulSoup as bs4
from splinter import Browser

username = input("Enter username (must be public) : ")
link = "https://www.instagram.com/"+username

if os.name == "posix":
	geckodriver_path = "./geckodriver/geckodriver"
else:
	geckodriver_path = "./geckodriver/geckodriver.exe"

with Browser("firefox",headless=True, executable_path=geckodriver_path) as browser:
	browser.visit(link)
	html = browser.html
	soup = bs4(html,"html.parser")

data = soup.findAll("img")
for x in data:
	x = x.get("src")
	os.system("wget --no-check-certificate -c -N -P ./Images/"+username+" "+x)
