from bs4 import BeautifulSoup as bs
import requests


class Songs:
    def __init__(self, name: str):
        self.url: str = 'https://songtranslate.ru/'
        self.name: str = name

    def popular_songs(self) -> tuple:
        page = bs(requests.get(self.url).content, 'html.parser')
        popular_songs: list = [
            tag.text.replace('\n', '') for tag in
            page.find('div', {'class': 'cols'})
            .find_all('div', {'class': 'col'})[0].find('ul', {'class': 'song-list'})
            .find_all('li')
        ]
        new_songs: list = [
            tag.text.replace('\n', '') for tag in
            page.find('div', {'class': 'cols'})
            .find_all('div', {'class': 'col'})[1].find('ul', {'class': 'song-list'})
            .find_all('li')
        ]
        top_songs: list = [
            tag.text.replace('\n', '').replace('0', '') for tag in
            page.find('div', {'class': 'cols'})
            .find_all('div', {'class': 'col'})[2].find('ul', {'class': 'song-list'})
            .find_all('li')
        ]
        return popular_songs, new_songs, top_songs

    def search_hrefs(self):
        checked_name: str = self.check_name(self.name)
        search: str = f'/search?q={checked_name}'
        search_hrefs: list = [
            link['href'] for link in bs(requests.get(self.url + search).content, 'html.parser')
            .find('div', {'class': 'content'})
            .find_all('a')
            if ('/songs' in link['href']) and ('.html' not in link['href']) and ('_and_' not in link['href'])
        ]
        return search_hrefs

    def search_artists(self) -> dict:
        search_hrefs: list = self.search_hrefs()
        bio: list = [
            bs(requests.get(self.url + href).content, 'html.parser')
            .find('div', {'class': 'bio'}).find('p').text
            for href in search_hrefs
        ]
        artists: list = self.search_names(search_hrefs)
        return dict(zip(artists, bio))

    @staticmethod
    def check_name(name: str) -> str:
        if len(name) == 0:
            raise ValueError('Поле ввода пустое.')
        return ' '.join(x.lower() for x in name.split(' '))

    @staticmethod
    def search_names(hrefs: list) -> list:
        result: list = []
        for href in hrefs:
            if '?' in href:
                del href
            else:
                replaced: str = href.replace('/songs/', '').replace('/', '')
                name: str = ' '.join([x.capitalize() for x in replaced.split('_')])
                result.append(name)
        return result

    def name_to_href(self):
        return '_'.join([x.lower() for x in self.name.split(' ')])

    def search_songs(self):
        search_hrefs: list = self.search_hrefs()
        name = self.name_to_href()
        artist_hrefs_songs: str = [
            bs(requests.get(self.url + href).content, 'html.parser')
            for href in search_hrefs if name in href
        ][0]
        songs = [
            x.text for x in
            artist_hrefs_songs.find('div', {'class': 'songs'}).find_all('a')
        ]
        print(songs)
        try:
            img = artist_hrefs_songs.find('div', {'class': 'img-wrap'}).find('img')['src']
            return img, songs
        except AttributeError:
            return songs


Songs('Michael Jackson').search_songs()
