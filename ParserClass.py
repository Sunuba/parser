import requests
from lxml import html
import re
import datetime


class Parser():
    def __init__(self, link):
        self.link = link

    @staticmethod
    def get_headers():
        return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def create_tree(self):
        headers = self.get_headers()
        page = requests.get(self.link, headers=headers)
        return html.fromstring(page.content)

    def get_data(self, html_code):
        tree = self.create_tree()
        return tree.xpath(html_code)
