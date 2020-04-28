from __future__ import print_function
import sys, os
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, "%dx%" % im.size, im.mode)
    except IOError:
        pass