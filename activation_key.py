#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
https://github.com/Yixiaohan/show-me-the-code
第0001题改动后的题目：
作为 App 独立开发者，你要搞限时促销，为你的应用生成10位包含随机数字或字母的激活码，如何生成 5 个激活码（或者优惠券）？
"""

import random
import string

class ActivationKey(object):
    def __init__(self):
        self.AVAILABLE_LETTERS = string.ascii_letters + string.digits
        self.KEY_LENGTH = 10
        self.KEY_COUNT = 5

    def generate_key_by_sample(self):
        return ''.join(random.sample(self.AVAILABLE_LETTERS, self.KEY_LENGTH))

    def generate_key_by_choice(self):
        key = ''
        for i in range(self.KEY_LENGTH):
            key += random.choice(self.AVAILABLE_LETTERS)
        
        return key

    def generate_key_by_randint(self):
        key = []
        available_letters_length = len(self.AVAILABLE_LETTERS)
        for i in range(self.KEY_LENGTH):
            letter = self.AVAILABLE_LETTERS[random.randint(0, available_letters_length - 1)]
            key.append(letter)

        return ''.join(key)

    def generate_key_by_choice_and_randint(self):
        key = []
        for i in range(self.KEY_LENGTH):
            letter = ''
            if random.randint(0,1) == 1:
                letter = random.choice(string.ascii_letters)
            else:
                letter = random.choice(string.digits)

            key.append(letter)

        return ''.join(key)

    def generate_keys(self, generate_method, save_method):
        keys = [ generate_method() for i in range(0, self.KEY_COUNT)]
        save_method(keys)

if __name__ == '__main__':
    activation_key = ActivationKey()
    activation_key.generate_keys(activation_key.generate_key_by_sample, print)
    activation_key.generate_keys(activation_key.generate_key_by_choice, print)
    activation_key.generate_keys(activation_key.generate_key_by_randint, print)
    activation_key.generate_keys(activation_key.generate_key_by_choice_and_randint, print)

