#!/bin/sh 

sh ./fileList.sh
echo 'videoToFrame start'
/root/.conda/envs/songjiyang/bin/python /root/songjiyang/task/seg/VideoToFrame.py
echo 'videoToFrame over'
sh ./fileList.sh
echo 'finish'

exit 0