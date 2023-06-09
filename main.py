import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


def parse_site(name: str):
    url = 'https://lyrsense.com'
    response = bs(requests.get(url + f'/search?s={name}&search=').content, 'html.parser')
    link = response.find('div', {'class': 'linkDiv'})['href']
    pass


parse_site('Beatles')
