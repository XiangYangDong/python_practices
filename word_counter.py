#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import re

'''
https://github.com/Yixiaohan/show-me-the-code
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

def create_test_file():
    filePath = r'D:\test.txt'
    testContents = 'In a calm sea, every man is a pilot. \r\n \
        But all sunshine without shade,all pleasure without pain, is not life at all. \
        Take the lot of happiest--it is a tangledyarn. \
        Bereavements and blessings,one following another, \
        make us sad and blessed by turns.Even death itself makes life more loving. \
        Men come closest to their true selves in the sober moments of life, \
        under the shadows of sorrow and loss. \r\n \
        In the affairs of life or of business, \
        it is not intellect that tells so much as character, \
        not brains so much as heart ,not genius so much as self-control, \
        patience,and discipline,regulated by judgment.'

    with open(filePath, 'w') as file:
        file.write(testContents)

    return filePath

def parse_words(filePath):
    with open(filePath, 'r') as file:
        fileContents = file.read()
        return re.findall(r'[a-zA-Z]+', fileContents)

if __name__ == '__main__':    
    filePath = create_test_file()
    words = parse_words(filePath)

    counts = {}
    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    
    print(counts)