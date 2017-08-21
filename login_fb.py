#! /usr/bin/python3

from selenium import webdriver
import getpass

link = "https://www.facebook.com"
email = input("Enter your email : ")
psswd = getpass.getpass("Enter password : ")


browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
browser.get(link)
mail = browser.find_element_by_name("email")
mail.send_keys(email)
pwd = browser.find_element_by_name("pass")
pwd.send_keys(psswd)

bttn = browser.find_element_by_id("loginbutton")
bttn.click()
