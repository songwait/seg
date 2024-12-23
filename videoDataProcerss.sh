#!/bin/sh 

sh ./fileList.sh
echo 'videoToFrame start'
python -u "VideoToFrame.py"
echo 'videoToFrame over'
sh ./fileList.sh
echo 'finish'

exit 