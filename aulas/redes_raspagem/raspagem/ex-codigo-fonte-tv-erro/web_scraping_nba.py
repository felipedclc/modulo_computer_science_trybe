import time

# -*- encoding: utf-8 -*-


import requests
import json
from parsel import Selector 

url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season=2020-21&SeasonType=Playoffs"

response = requests.get(url)
