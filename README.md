# carparkingmonitoringsystem
This information system will provide people with more ideas on how many available places on each car parks.
website: https://bottles.github.io/

Prerequisite: Tensorflow, kafka, python2.7, google street view api key.

The system has been designed to have been built on cloud system. It has several parts: 
- cloud/: configuration of cloud system
- work/detect/: get car images from google imageview or from monitor
- work/identify/: use tensorflow or other AI technology to regonise a car
- message/kafka/: distributed system messaging package
- website/: Golang website to show the final result
- carparks.db: for temporarily store data of car parking place

How to run demo:
# step1. get the image from google street view and crop the image
cd carparking/work/detect
python detectCars.py

# step2. generate the empty parking result from the cropped image
cd carparking/work/identify
./process_data_empty.sh

# or step2. generate the full parking result from the cropped image
cd carparking/work/identify
./process_data_full.sh

# go to web demo directory; this will show if a car parking place is available or not on the google map
cd carparking/website/src/car-parking-python-simple-demo
python demo.py
