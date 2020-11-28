from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup as soup
import sys
import json
from datetime import datetime

apoop = "https://www.youtube.com/c/milosh9k/videos"

r = requests.get(apoop)
page = r.text
soup = soup(page,'html.parser')
containers = soup.find_all('a',{'class':'yt-simple-endpoint inline-block style-scope ytd-thumbnail'})

for container in containers:
    print(container)

