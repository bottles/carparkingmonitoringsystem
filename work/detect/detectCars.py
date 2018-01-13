
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


def crop_by_loc(input, img_id, r1, r2, r3, r4):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    box = (r1, r2, r3, r4)
    a = im.crop(box)
    print(a)
    try:
        a.save("IMG-%d.jpg" % img_id)
    except:
        print ("There is an error")

data = json.load(open('../../carparks.db'))
anu_car_park = data["carparks"][0]

urllib.urlretrieve("http://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + anu_car_park["location"] + "&pitch=" + anu_car_park["pitch"] + "&key=" + data["key"],"1.1.jpg")

print("http://maps.googleapis.com/maps/api/streetview?size=600x    300&location=" + anu_car_park["location"] + "&pitch=" + anu_car_park["pitch"    ] + "&key=" + data["key"],"1.1.jpg")


crop_by_loc("1.1.jpg", 1, 70, 150, 170, 250)
crop_by_loc("1.1.jpg", 2, 170, 150, 270, 250)
crop_by_loc("1.1.jpg", 3, 270, 150, 370, 250)
crop_by_loc("1.1.jpg", 4, 370, 202, 470, 302)

