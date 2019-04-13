#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# file name : image_spider.py
# author by : xiangyang

import requests
import re
import os
import time
import random

class UnsplashDownloader(object):
    def __init__(self):
        self.image_folder = 'E:/pictures'
        self.image_url_template = 'https://unsplash.com/photos/{}/download'
        self.categories = ['wallpapers', 'animals']
        self.page_limit = 2
        self.headers ={ 'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN',
               'Cache-Control': 'no-cache',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134' } 

    def download_images(self):
        if len(self.categories) == 0:
            return

        if not(os.path.exists(self.image_folder)):
            os.makedirs(self.image_folder)

        for category in self.categories:
            self.download_category_images(category)

    def download_category_images(self, category):
        category_image_folder = os.path.join(self.image_folder, category)
        if not(os.path.exists(category_image_folder)):
            os.makedirs(category_image_folder)

        i = 1
        for page in range(1, self.page_limit + 1):
            url = 'https://unsplash.com/napi/search/photos?query=' + category + '&xp=&per_page=20&page='+str(page)
            response = requests.get(url, headers = self.headers)
            pattern = '\"download\":\"https://unsplash.com/photos/(.*?)/download\"'
            matches = re.findall(pattern, response.text, re.S)
            for id in matches:
                time.sleep(random.uniform(0,3))

                try:
                    print('downloading {}th image...'.format(i))

                    image_file = requests.get(self.image_url_template.format(id), headers = self.headers)
                    image_file_path = os.path.join(category_image_folder, id + '.jpg')
                    with open(image_file_path, 'wb') as f:
                        f.write(image_file.content)
                    print('download {}th image done!'.format(i))
                except:
                    print('download {}th image failed!'.format(i))
                
                i = i + 1

if __name__ == '__main__':
    image_downloader = UnsplashDownloader()
    image_downloader.download_images()