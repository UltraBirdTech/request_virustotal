#!bin/sh

echo 'copy folder is start.'
cp /data/cowire/donwloads.*.gz /home/honey/downloads/
echo 'copy folder is finish.'

echo 'create tar file start.'
tar -zxcf downloads.tar.gz /home/honey/donwloads/
echo 'create tar file finsih.'
