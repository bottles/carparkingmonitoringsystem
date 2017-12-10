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
