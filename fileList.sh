#!/bin/sh 
cat>data/video.txt<<EOF
$(ls data -1 -R | grep mp4| while read line
do 
find -name $line &
done) 
EOF
cat>data/frame.txt<<EOF
$(ls  -1 -R | grep png| while read line
do 
find -name $line &
done) 
EOF

exit 0
