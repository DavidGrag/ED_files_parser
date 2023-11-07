import os
import requests
from bs4 import BeautifulSoup


class Parser:

    __n: int
    __page: int

    def __init__(self, url):
        self.__url = url
        self.__n = 1
        self.data = []
        self.__page = 1
        self.__pages = self.__get_pages_count()

    @staticmethod
    def __get_page(url, page):
        full_url = f'{url}{page}'
        html = requests.get(full_url)
        req = html.text
        soup = BeautifulSoup(req, 'html.parser')
        bodies = soup.find_all(class_='file-body')
        return soup, bodies

    def __get_pages_count(self):
        soup = self.__get_page(self.__url, 1)[0]
        pagination = soup.find(class_='pagination').select('a')[-2].text
        pages = int(pagination)
        return pages

    def parsing(self, show_info=False):
        while self.__page <= self.__pages:
            if show_info:
                self.__show_info()
            self.__parse_page()
            self.__page += 1

    def __parse_page(self):
        bodies = self.__get_page(self.__url, self.__page)[1]
        for body in bodies:
            mod_data = []
            well = body.parent()
            try:
                version = well[1].text.strip()
            except ValueError:
                version = None
            try:
                aircraft = well[3].text.strip()
            except ValueError:
                aircraft = None

            nopd = body.find(class_='no-padding')
            name = nopd.select('a')[0]

            file_info = body.find(class_='list-unstyled')
            size = file_info.select('li')[2].text
            try:
                if size[-2:] == 'Мб':
                    float_size = float(size[14:-2])
                    size = float_size * 1024
                elif size[-2:] == 'Кб':
                    size = float(size[14:-2])
                else:
                    size = float(size[14:-4])
            except ValueError:
                size = None

            upload_date = body.find(class_='date').text.strip()[7:-9]
            downloads_count = file_info.select('li')[3].text[9:]
            mod_name = name.text.strip()
            author = body.find(class_='author').select('a')[0]
            mod_author = author.text.strip()
            license_text = file_info.select('li')[0].text[41:]
            mod_livery_link = 'https://www.digitalcombatsimulator.com' + name['href']

            mod_data.append(mod_name)
            mod_data.append(mod_livery_link)
            mod_data.append(mod_author)
            mod_data.append(size)
            mod_data.append(upload_date)
            mod_data.append(downloads_count)
            mod_data.append(aircraft)
            mod_data.append(version)
            mod_data.append(license_text)
            self.data.append(mod_data)
            self.__n += 1

    def __show_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Mod #{self.__n}')
        print(f'Page {self.__page} of {self.__pages}')

