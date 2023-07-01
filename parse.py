from bs4 import BeautifulSoup as bs
import requests


class Songs:
    def __init__(self, name: str):
        self.url: str = 'https://songtranslate.ru/'
        self.name = name

    def popular_songs(self):
        page = bs(requests.get(self.url).content, 'html.parser')
        popular_songs = [
            x.text.replace('\n', '') for x in
            page.find('div', {'class': 'cols'})
            .find_all('div', {'class': 'col'})[0].find('ul', {'class': 'song-list'})
            .find_all('li')
        ]
        new_songs = [
            x.text.replace('\n', '') for x in
            page.find('div', {'class': 'cols'})
            .find_all('div', {'class': 'col'})[1].find('ul', {'class': 'song-list'})
            .find_all('li')
        ]
        top_songs = [
            x.text.replace('\n', '').replace('0', '') for x in
            page.find('div', {'class': 'cols'})
            .find_all('div', {'class': 'col'})[2].find('ul', {'class': 'song-list'})
            .find_all('li')
        ]
        return popular_songs, new_songs, top_songs

    def search_songs(self):
        checked_name = self.check_name(self.name)
        search: str = f'/search?q={checked_name}'
        search_hrefs = [
            x['href'] for x in bs(requests.get(self.url + search).content, 'html.parser')
            .find('div', {'class': 'content'})
            .find_all('a')
            if '/songs' in x['href']
        ]
        artists = self.search_names(search_hrefs)

    @staticmethod
    def check_name(name: str) -> str:
        name_list = ' '.join(x.lower() for x in name.split(' '))
        return name_list

    @staticmethod
    def search_names(hrefs: list) -> list:
        result = []
        for href in hrefs:
            if '?' in href:
                del href
            else:
                replaced = href.replace('/songs/', '').replace('/', '')
                name = ' '.join([x.capitalize() for x in replaced.split('_')])
                result.append(name)
        return result


Songs('Lil UZI').popular_songs()
