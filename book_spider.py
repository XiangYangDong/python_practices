#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# file name : book_spider.py
# author by : xiangyang

from bs4 import BeautifulSoup
from sys import stdout
import requests
import sys
import time

"""
Class definition : download the ebook from the web 'https://www.biquge.cc/'
"""
class BookDownloader(object):
    def __init__(self):
        self.target = 'https://www.biquge.cc/html/6/6551/'
        self.headers ={ 'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN',
               'Cache-Control': 'no-cache',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134' }
        self.names = []
        self.urls = []
        self.numbers = 0

    """
    Method definition : get download urls from the chapter list page
    Parameters:
        None
    Returns:
        None
    """    
    def get_download_urls(self):
        req = requests.get(url = self.target, headers = self.headers)
        html = req.text
        div_bf = BeautifulSoup(html, features='lxml')
        div = div_bf.find('div', id = 'list')
        a_bf = BeautifulSoup(str(div), features='lxml')
        a = a_bf.find_all('a')
        chapter_parts = a[15:] #remove useless parts
        self.numbers = len(chapter_parts) 
        for each in chapter_parts:
            self.names.append(each.string)
            self.urls.append(self.target+each.get('href'))

    """
    Method definition : get chapter contents from the detail page
    Parameters:
        target - detail page url (string)
    Returns:
        chapter_contents - chapter contents (string)
    """    
    def get_chapter_contents(self, target):
        req = requests.get(url = target, headers = self.headers)
        html = req.text
        bf = BeautifulSoup(html, features='lxml')
        chapter_contents = bf.find('div', id = 'content').text.replace(\
                                  '\xa0'*4, '\n')
        return chapter_contents
    
    """
    Method definition : write the chapter name and contents to a file
    Parameters:
        name - chapter name (string)
        path - file path to write (string)
        text - chapter contents (string)
    Returns:
        None
    """
    def write(self, name, path, text):
        with open(path, 'a', encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    downloader = BookDownloader()
    downloader.get_download_urls()
    print('《琅琊榜》开始下载：')
    for i in range(downloader.numbers):
        downloader.write(downloader.names[i], r'D:\Books\琅琊榜.txt', \
                         downloader.get_chapter_contents(downloader.urls[i]))
        stdout.write(' 已下载:%.1f%%\n' %  float(i * 100 / downloader.numbers))
        stdout.flush()
    print('《琅琊榜》下载完成')