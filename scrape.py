import requests
import json
import sys
import time
import math
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

driver = webdriver.Firefox()



driver.quit()
