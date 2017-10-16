#!/bin/bash
cd '/Volumes/MacintoshHD/_GitHub/gas'
rsync -avzh pi@192.168.1.135:/media/pi/RAI/logs/gasolineras/ /Volumes/MacintoshHD/_data/gasolineras/
echo "Generate map...."
python generate_map.py
git pull
git add *
git commit -m "Added new map"
git push origin master
echo "Finish"
