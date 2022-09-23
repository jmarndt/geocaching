import json
import requests
from bs4 import  BeautifulSoup


with open(".auth.json", "r",) as auth_file:
    auth_json = json.loads(auth_file.read())
cookies = {'jwt': auth_json['gc_jwt']}
gc8kd18 = 'gc8kd18'
# page = requests.get(f'https://www.geocaching.com/geocache/{odd_or_even}', cookies=cookies)
# soup = BeautifulSoup(page.content, "html.parser")


##### TEMPORARY WHILE TESTING TO PREVENT EXTRA HTTP CALLS ########
# with open("gc8kd18.html", "w", encoding='utf-8') as file:
#     file.write(str(soup.prettify()))
with open("gc8kd18.html", "r", encoding='utf-8') as file:
    page = file.read()
soup = BeautifulSoup(page, "html.parser")
##### TEMPORARY WHILE TESTING TO PREVENT EXTRA HTTP CALLS ########


cache_title = soup.title.text.strip()
cache_name = soup.find("span", {"id":"ctl00_ContentBody_CacheName"}).text.strip() #id="ctl00_ContentBody_CacheName"
hidden_by = ''
owner_name = ''
date_hidden = ''
date_published = ''
cache_difficulty = ''
cache_terrain = ''
cache_size = ''
posted_coordinates = ''
corrected_coordinates = ''
cache_attributes = ''
background_img = ''
short_description = ''
long_description = ''
html_comments = ''
cache_hint = ''
cache_inventory = ''
bookmark_lists = ''


cache_analysis_report = f"""
{cache_title}
---
Cache Name: {cache_name}
Hidden by: {hidden_by} | Owner username: {owner_name}
Date hidden: {date_hidden} | Published on: {date_published}
Diffuculty: {cache_difficulty} | Terrain: {cache_terrain} | Size: {cache_size}
Posted coordinates: {posted_coordinates} | Corrected coordinates: {corrected_coordinates}
Background Image: {background_img}
Attributes:
{cache_attributes}
Description:
{short_description}
{long_description}
HTML comments:
{html_comments}
Cache hint:
{cache_hint}
Inventory:
{cache_inventory}
Bookmarks lists:
{bookmark_lists}
"""

print(cache_analysis_report)