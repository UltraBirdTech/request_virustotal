#!bin/bash
echo 'create downloads folder is start.'
mkdir ./downloads
echo 'create downloads foler is finished.'
echo 'copy folder is start.'
cp /data/cowrie/downloads.*.gz /home/honey/downloads/
echo 'copy folder is finish.'

echo 'create tar file start.'
tar -zcvf downloads.tar.gz ./downloads/
echo 'create tar file finsih.'
