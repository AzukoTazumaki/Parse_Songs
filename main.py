import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


def parse_site(name: str):
    url: str = 'https://lyrsense.com'
    search: str = f'/search?s={name}&search='
    artist_link = bs(requests.get(url + search).content, 'html.parser').find('div', {'class': 'linkDiv'})['href']
    albums = [
        x.text for x in bs(requests.get(url + artist_link).content, 'html.parser')
        .find_all('strong', {'class': 'albumTitle'})
    ]
    pass


parse_site('Beatles')
