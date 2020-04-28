from __future__ import print_function
#import sys, os
from PIL import Image

im = Image.open("./fotos/tutorial.png")

box = (100, 100, 100, 100)
region = im.crop(box)

region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

def roll(image, delta):
    """rolando uma imagen lateralment"""
    xsize, ysize, = image.size

    delta %= xsize
    if delta == 0: return image

    part1 = image.crop(0, 0, delta, ysize)
    part2 = image.crop(delta, 0, xsize, ysize)
    image.paste(part1, (xsize - delta, 0, xsize, ysize))
    image.paste(part1, (0, 0, xsize-delta, ysize))

    return image