import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from random import randint


def parse_site(name: str):
    url: str = 'https://songtranslate.ru/'
    search: str = f'/search?q={name}'
    search_hrefs = [
        x['href'] for x in bs(requests.get(url + search).content, 'html.parser')
        .find('div', {'class': 'content'})
        .find_all('a') if f'{ name.lower() }' in x['href']
    ]
    artists = search_names(search_hrefs)
    pass


def search_names(hrefs: list):
    result = []
    for href in hrefs:
        if '?' in href:
            del href
        else:
            replaced = href.replace('/songs/', '').replace('/', '')
            name = ' '.join([x.capitalize() for x in replaced.split('_')])
            result.append(name)
    return result


parse_site('Drake')
