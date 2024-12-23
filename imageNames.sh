#!/bin/sh 
cat>data/train.txt<<EOF
$(ls  data/dataSet/images/train -1 -R | grep png| while read line
do 
echo $line &
done) 
EOF

cat>data/val.txt<<EOF
$(ls  data/dataSet/images/val -1 -R | grep png| while read line
do 
echo $line &
done) 
EOF

exit 0