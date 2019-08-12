from PIL import Image
import os

phone_width = 1125
phone_height = 2436

image_path = r"E:\Test\IMG_20180928_182756.jpg"
im = Image.open(image_path)

image_width = im.size[0]
image_height = im.size[1]

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