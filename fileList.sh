#!/bin/sh 
cat>data/video.txt<<EOF
$(ls data/tennis/video -1 -R | grep mp4| while read line
do 
find data/tennis/video -name $line &
done) 
EOF
cat>data/frame.txt<<EOF
$(ls data/tennis/frame -1 -R | grep png| while read line
do 
find data/tennis/frame -name $line &
done) 
EOF

exit 0
