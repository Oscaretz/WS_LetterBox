from bs4 import BeautifulSoup
from requests_html import HTMLSession
import asyncio



class Cuevana:
    def __init__(self, theme):
        self.theme = theme
        self.movie_links = []
        self.i = 0

    def html_link_obtainer(self):

        session = HTMLSession()

        url = f'https://cuevana.biz/genero/{self.theme}/page/{self.i+1}'

        response = session.get(url)
        response.html.render()

        if response.status_code == 200:
            html = response.text

            soup = BeautifulSoup(html, 'html.parser')
            
            movie_link_elements = soup.find_all('div', class_='TPost C hentry')
            
            self.movie_links.append(link.a['href'] for link in movie_link_elements if link.a)
            self.i+=1

        else:
            return False