from bs4 import BeautifulSoup
from pprint import pprint
import urllib.request
import re
import requests
import json

def get_news(keywords):
    keyword = 'q='+re.sub(r"\s+", ' ', keywords)+'&'
    url = ('https://newsapi.org/v2/everything?'+keyword+'from=2020-08-01&sortBy=popularity&apiKey='+newsApiKey)
    res = (requests.get(url)).json()["articles"]
    newsTitles = []
    for news in res:
        newsTitles.append((news["title"]+".").lower())
    return newsTitles
