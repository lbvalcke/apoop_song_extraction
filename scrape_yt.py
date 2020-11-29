from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import sys
import json
from datetime import datetime

apoop = "https://www.youtube.com/c/milosh9k/videos"

r = requests.get(apoop)
page = r.text
parsed_page = BeautifulSoup(page,'lxml')
containers = parsed_page.find_all('script')

content = containers[28].get_text()
stripped_content = content[20:len(content)-1]
json_content = json.loads(stripped_content)

vid_list = []

for key in json_content['contents']['twoColumnBrowseResultsRenderer']['tabs']:    
    vid_list.append(key)

for vid in vid_list:
    for key in vid:
        print(key)


for item in vid_list[1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']: 
    url = item['gridVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    print(url)

