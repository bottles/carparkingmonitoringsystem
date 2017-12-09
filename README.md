# carparkingmonitoringsystem
This information system will provide people with more ideas on how many available places on each car parks.
website: https://bottles.github.io/

The system has been designed to have been built on cloud system. It has several parts: 
- cloud/: configuration of cloud system
- detectCars/: get car images from google imageview or from monitor
- identifyCars/: use tensorflow or other AI technology to regonise a car
- kafka/: distributed system messaging package
- website/: Golang website to show the final result
- carparks.db: for temporarily store data of car parking place
