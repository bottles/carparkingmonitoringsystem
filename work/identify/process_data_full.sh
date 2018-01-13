#!/bin/sh

python classify_image.py --image_file ../detect/IMG-1.jpg --num_top_predictions 1 > result
python classify_image.py --image_file ../detect/IMG-2.jpg --num_top_predictions 1 >> result
python classify_image.py --image_file ../detect/IMG-3.jpg --num_top_predictions 1 >> result


