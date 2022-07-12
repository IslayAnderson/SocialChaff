import requests
import json
import sys
import time
import math
import webbrowser
import intro
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

scratchJS = [line.rstrip('\n') for line in open('scratch.js')]
subjectsNormal = [line.rstrip('\n') for line in open('subjectsNormal.txt')]
subjectsWeird = [line.rstrip('\n') for line in open('subjectsWeird.txt')]
subjectsSuspicious = [line.rstrip('\n') for line in open('subjectsSuspicious.txt')]

peopleNormal = [line.rstrip('\n') for line in open('peopleNormal.txt')]
peopleWeird = [line.rstrip('\n') for line in open('peopleWeird.txt')]
peopleSuspicious = [line.rstrip('\n') for line in open('peopleSuspicious.txt')]

thingsNormal = [line.rstrip('\n') for line in open('thingsNormal.txt')]
thingsWeird = [line.rstrip('\n') for line in open('thingsWeird.txt')]
thingsSuspicious = [line.rstrip('\n') for line in open('thingsSuspicious.txt')]

adlibsPeople = [line.rstrip('\n') for line in open('adlibsPeople.txt')]
adlibsThings = [line.rstrip('\n') for line in open('adlibsThings.txt')]
adlibsSubjects = [line.rstrip('\n') for line in open('adlibssubjects.txt')]

ruinmysearchhistory = [line.rstrip('\n') for line in open('ruinmysearchhistory.txt')]
#for the memes

intro.intro()

time.sleep(1)
webbrowser.open('https://www.whatsmyua.info/')
userAgent = input("Enter userAgent:")
print("")
print("0: Normal")
print("1: Weird")
print("2: Suspicious")
weirdScale = input("Select your level of weird:")
print("")
print("0: Things")
print("1: People")
print("2: Subjects")
print("3: All")
print("4: ruinmysearchhistory.com list, because funny")
criteria = input("Select your criteria:")
print("")
print("0: twitter")
print("1: youtube")
print("2: facebook")
print("3: instagram")
print("4: All")
socialMedia = input("Select your social media:")



driver = webdriver.Firefox()



driver.quit()
