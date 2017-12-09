import PIL
from PIL import Image
import os, sys
rootdir = '/Users/jengao/Project/models/tutorials/image/imagenet/car/'


basewidth = 300

index=0
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		index = index+1
		img = Image.open(rootdir+file)
		wpercent = (basewidth / float(img.size[0]))
		hsize = int((float(img.size[1]) * float(wpercent)))
		img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
		img.save(str(index) + ".jpg")
		os.system("aws s3 cp "+str(index) + ".jpg s3://cf-templates-1j1kft5x809hp-ap-southeast-2")
		os.system("rm -rf " + str(index)+".jpg")
