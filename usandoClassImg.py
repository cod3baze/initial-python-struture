from __future__ import print_function
from PIL import Image

#im = Image.open("./fotos/tutorial.png")
#print(im.format, im.size, im.mode)


img = list()

img.append(Image.open("./fotos/tutorial.png"))
img.append(Image.open("./fotos/learn.png"))
img.append(Image.open("./fotos/wrapper.png"))

print(len(img))

for i in img:
    print(i.format, i.size, i.mode)

print("feito")


