#!/bin/sh 

./fileList.sh
echo 'videoToFrame start'
python -u "c:\Users\Administrator\Desktop\seg\VideoToFrame.py"
echo 'videoToFrame over'
./fileList.sh
echo 'finish'

exit 0bash