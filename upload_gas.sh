#!/bin/bash
cd '/Volumes/Macintosh HD/_GitHub/gas'
python generate_map.py
git add *
git commit -m "Added new map"
git push origin master
echo "Finish"
