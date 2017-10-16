#!/bin/bash
cd '/Volumes/Macintosh HD/_GitHub/gas'
rsync -avzh pi@192.168.1.135:/media/pi/RAI/logs/gasolineras/ /Volumes/Macintosh\ HD/_data/gasolineras/ -p 'J4v5f7o3'
python generate_map.py
git add *
git commit -m "Added new map"
git push origin master
echo "Finish"
