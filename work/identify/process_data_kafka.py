import os

import sys
import subprocess


event_id = sys.argv[1]

p = subprocess.Popen('python classify_image.py --image_file ../detect/IMG-' + event_id + '.jpg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

i = 0
for line in p.stdout.readlines():
    if i == 2:
        result = line
        break
    i += 1

retval = p.wait()

p = subprocess.Popen('python ../../message/kafka/producer.py "' + str(result) + '"', shell=True)





