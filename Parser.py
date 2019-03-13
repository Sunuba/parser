#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html
import random


class Parser():
    def __init__(self, link, use_proxy=False):
        self.link = link
        self.use_proxy = use_proxy

    @staticmethod
    def get_headers():
        return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def handle_proxy(self):
            return self.create_tree()

    def create_tree(self):
        headers = self.get_headers()
        page = requests.get(self.link, headers=headers)
        if self.use_proxy:
            page = requests.get(self.link, headers=headers, proxies=self.proxy())
        return html.fromstring(page.content.decode('utf-8'))

    def get_data(self, html_code):
        tree = self.handle_proxy()
        return tree.xpath(html_code)

    def prepare(self, string):
        parts = string.split('.')
        if len(parts) == 3:
            element = parts[0]
            tag = parts[1]
            name = parts[2]
            return '/'+element+'[contains('+tag+', "'+name+'")]'
        else:
            return '/' + string

    def prepare_sections(self, string, indicator):
        sections = string.split('/')
        final_code = '/'
        for section in sections:
            final_code = final_code + self.prepare(section)
        return final_code + '/' + indicator

    def proxy(self):
        sec_conv = {'yes':'https', 'no':'http'}
        list_proxy = {}
        parser = Parser('https://free-proxy-list.net')
        ip_route = 'table.@id.proxylisttable/tbody/tr/td[1]'
        port_route = 'table.@id.proxylisttable/tbody/tr/td[2]'
        security_route = 'table.@id.proxylisttable/tbody/tr/td[7]'
        ip_prepare = parser.prepare_sections(ip_route, 'text()')
        port_prepare = parser.prepare_sections(port_route, 'text()')
        security_prepare = parser.prepare_sections(security_route, 'text()')
        table_data = parser.get_data(ip_prepare)
        port_data = parser.get_data(port_prepare)
        security_data = parser.get_data(security_prepare)
        proxy_list = list(zip(table_data, port_data, security_data))
        random_number = random.randint(0, len(proxy_list))
        single_proxy = proxy_list[random_number]
        protocol = sec_conv[single_proxy[2]]
        single_proxy = protocol + "://" + single_proxy[0]+":"+single_proxy[1]
        list_proxy[protocol] = single_proxy
        return list_proxy
