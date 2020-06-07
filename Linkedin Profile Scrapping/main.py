import requests
import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome("driver/chromedriver")
browser.get("https://www.linkedin.com/uas/login")
file = open("config.txt")
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id("username")
elementID.send_keys(username)

elementID = browser.find_element_by_id("password")
elementID.send_keys(password)

elementID.submit()

link = "https://www.linkedin.com/in/1209simran/"
browser.get(link)

src = browser.page_source
soup = BeautifulSoup(src, 'html.parser')

filename = "Details.csv"
f = open(filename, "w")
headers = "Name, Intro, Place,Connections \n"
f.write(headers)

container = soup.find("div", class_="flex-1 mr5")
name_div = container.find_all('ul')
name = name_div[0].find("li").text.strip()
# print(name)
intro_div = container.find_all("div")
intro = intro_div[0].find("h2").text.strip()
# print(intro)
place_div = name_div[1].find_all("li")
place = place_div[0].text.strip()
# print(place)
connections = place_div[1].text.strip()
# print(connections)
f.write(name.replace(",", "")+"," + intro.replace(",", "") +
        ","+place.replace(",", " |")+","+connections+"\n")
f.close()
