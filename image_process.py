from PIL import Image
import os

'''
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhoneX 分辨率的大小。
'''

def resize_image(image_path):
    im = Image.open(image_path)
    image_width = im.size[0]
    image_height = im.size[1]
    
    phone_width = 1125
    phone_height = 2436
    real_width = 0
    real_height = 0
    
    if image_width / image_height >= phone_width / phone_height:
        real_width = phone_width
        real_height = int(image_height * phone_width / image_width)
    else:
        real_width = int(image_width * phone_height / image_height)
        real_height = phone_height
    
    path_texts = os.path.splitext(image_path)
    thumbnail_path = path_texts[0] + ".thumbnail" + path_texts[1]
    im.thumbnail((real_width, real_height))
    im.save(thumbnail_path)

if __name__ == '__main__':
    images_folder = r"E:\Test"
    for dir_name, dirs, image_names in os.walk(images_folder):
        for image in image_names:
            image_path = os.path.join(dir_name, image)
            resize_image(image_path)