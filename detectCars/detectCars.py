
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os.path
import re
import sys
import tarfile

import numpy as np
from six.moves import urllib
#import tensorflow as tf
import urllib

import json
from pprint import pprint
import os

from PIL import Image



def crop(Path, input, height, width, k, page):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            print (a)
            try:
                #o = a.crop(area)
                a.save("IMG-%d.jpg" % k)
            except:
		        print ("sth wrong")
            k +=1



data = json.load(open('../carparks.db'))
anu_car_park = data["carparks"][0]

urllib.urlretrieve("http://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + anu_car_park["location"] + "&pitch=" + anu_car_park["pitch"] + "&key=" + data["key"],"1.1.jpg")


crop("./", "1.1.jpg", 100, 100, 9, "hello")




